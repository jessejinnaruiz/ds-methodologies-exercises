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
import acquire_mall
from acquire_mall import get_mall_data

mall_df = get_mall_data()
# print(mall_df)


print('------------------')
#Create some functions to prepare data

#Detects any outliers
def get_upper_outliers(df):
    '''
    Given a series and a cutoff value, k, returns the upper outliers for the
    series.

    The values returned will be either 0 (if the point is not an outlier), or a
    number that indicates how far away from the upper bound the observation is.
    '''
    k= 1.5
    q1, q3 = s.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + k * iqr
    for col in df:
        if df.dtype == 'number' or 'float':
            return col.apply(lambda x: max([x - upper_bound, 0]))
        else:
            continue


def add_upper_outlier_columns(df):
    '''
    Add a column with the suffix _outliers for all the numeric columns
    in the given dataframe.
    '''
    # outlier_cols = {col + '_outliers': get_upper_outliers(df[col], k)
    #                 for col in df.select_dtypes('number')}
    # return df.assign(**outlier_cols)

    for col in df.select_dtypes('number'):
        df[col + '_outliers'] = get_upper_outliers(df[col])
    return df


#Encodes all the categorical columns, and adds the encoded column (i.e. it doesn't remove the original column)
from sklearn import preprocessing
def encoder(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            encoder = preprocessing.LabelEncoder()
            encoder.fit(mall_df[col])
            mall_df[col+'_encoded'] = encoder.transform(mall_df[col])
        else:
            continue


#Accepts the unprepared mall customers data frame and applies all the transformations above.
def prep_mall(df):
    return mall_df.pipe(get_upper_outliers())\
        .pipe(add_upper_outlier_columns())\
        .pipe(encoder())


# Summarize the data:

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