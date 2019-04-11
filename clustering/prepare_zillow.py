# Import libraries
# ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Wrangling
import pandas as pd
import numpy as np

# Exploring
import scipy.stats as stats

# Visualizing
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

# default pandas decimal number display format
pd.options.display.float_format = '{:20,.2f}'.format

#Import data
import acquire_zillow
from acquire_zillow import get_zillow_data_2016
from acquire_zillow import save_df_2016
from acquire_zillow import get_zillow_data_2017
from acquire_zillow import save_df_2017

df_2016 = get_zillow_data_2016()
# save_df_2016()
df_2017 = get_zillow_data_2017()
# save_df_2017
print('------------------')


# Summarize Data
def peekatdata(df):
    print("\nRows & Columns:\n")
    print(df.shape)
    print("\nColumn Info:\n")
    print(df.info())
    print("\nFirst 5 rows:\n")
    print(df.head())
    print("\nLast 5 rows:\n")
    print(df.tail())
    print("\nMissing Values:\n")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())
    print("\nSummary Stats:\n")
    print(df.describe())
    return df

def df_value_counts(df):
    for col in df.columns: 
        n = df[col].unique().shape[0] 
        col_bins = min(n,10) 
        if df[col].dtype in ['int64','float64'] and n > 10:
            print('%s:' % col)
            print(df[col].value_counts(bins=col_bins, sort=False)) 
        else: 
            print(df[col].value_counts()) 
        print('\n')
    return df

def percent_missing(df):
    missing_table = df.isnull().sum()/df.shape[0]*100
    return df


peekatdata(df)
df_value_counts(df)
percent_missing(df)


# Clean data
# Cleans up the extra columns from initial SQL queries
for col in drop_id_cols:
    df_2017 = df_2017.drop(col, axis=1)

for col in drop_id_cols:
    df_2016 = df_2016.drop(col, axis=1)


# Concatenates 2016 and 2017 df
df = pd.concat([df_2016, df_2017], axis=0)
df.tail()

#include only single unit properties (e.g. no duplexes, no land/lot, ...) 
def single_unit_properties(df):
    df_single_units = df[(df.unitcnt == 1) & (df.bathroomcnt >0)]
    return df_single_units

df_single_units.shape


# Takes in a dataframe and a list of columns names and returns the dataframe with the 
# datatypes of those columns changed to a non-numeric type

num_to_cat_cols = ['regionidcity', 'regionidcounty','regionidneighborhood', 'regionidzip','yearbuilt', 'assessmentyear', 'taxdelinquencyyear','fireplaceflag','censustractandblock']

def convert_numeric(df):
    list = num_to_cat_cols
    for col in list:
        df[col] = df[col].astype(str)
    return df    

# Handle Missing Values
# Calculates by columns
def amt_missing(df):
    percentage_missing = df.isnull().sum()/df.shape[0]*100
    number_missing = df.isnull().sum()
    amt_missing = list(zip(percentage_missing, number_missing))
    df = pd.DataFrame(amt_missing, columns=['Percentage Missing', 'Number of Missing Values'])
    return df
# Calculate by rows
def amt_missing_rows(df):
    null_count = df.isnull().sum(axis=1)
    null_percentage = (null_count / df.shape[1]) * 100
    return pd.DataFrame({'num_missing': null_count, 'percentage': null_percentage})

# Save the amounts missing information in a new dataframe
df_missing_cols = amt_missing(df_single_units)
df_missing_cols['Column Name'] = [x for x in df_single_units.columns]
df_missing_cols

# Drop columns that have 100% null values
# These columns have 100% null values, so we can drop them all together.
drop_null_cols = df_missing_cols[(df_missing_cols['Percentage Missing'] == 100.0 )]['Column Name'].tolist()
drop_null_cols

df_single_units = df_single_units.drop(columns=drop_null_cols, axis=0)
df_single_units.columns

# Take null values and input 0
def input_zeros(df, cols):
    for col in cols:
        df[col].fillna(0, inplace=True)
    return df

# These columns have some missing values.
replace_nulls = df_missing_cols[(df_missing_cols['Percentage Missing'] > 0 ) & (df_missing_cols['Percentage Missing'] < 100 )]['Column Name'].tolist()
replace_nulls

input_zeros(df_single_units, replace_nulls)

# Impute the values in land square feet.
