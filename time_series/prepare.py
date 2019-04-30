"""Prepare script for Time Series Analysis Module
Jesse Jinna Ruiz
2019
"""

import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt

from acquire import get_all_data


test_dates = pd.DataFrame(data={'date': ['08/08/88','08/09/1988','08/10/1988','08/11/1988']})
test_dates

pd.to_datetime(test_dates['date'])

df = get_all_data()


# ####  A function to convert a date to a datetime data type. Accepts string, list, or pd.Series
# 


def convert_to_datetime(date):
    return pd.to_datetime(date, format = "%m/%d/%y", infer_datetime_format=True)


convert_to_datetime('08/08/88')


pd.to_datetime(test_dates['date'])


# #### A function to change a datetime to UTC. Accepts string, list, or pd.Series


def convert_to_utc(date):
    return pd.to_datetime(date, utc=True)




# #### A function to parse a date column into 6 additional columns (while keeping the original date): year, quarter, month, day of month, day of week, weekend vs. weekday
# 
def parse_date(date):
    new_date = pd.to_datetime(date)
    return pd.DataFrame(data={'date_original': new_date,'year': new_date.dt.year, 'quarter': new_date.dt.quarter, 'month': new_date.dt.month,'day_of_month': new_date.dt.day, 'day_of_week': new_date.dt.weekday_name, 'is_weekend':  new_date.dt.weekday_name.str.startswith('S')})


parse_date(test_dates['date'])


# #### Add a column to dataframe, sales_total, which is a derived from sale_amount (total items) and item_price.

df.groupby('sale_id').tail(20)

for col in df.columns:
    print(col,':', df[col].dtype)


df['sales_total'] = df['sale_amount'] * df['item_price']



# #### Create a new dataframe that aggregates the sales_total and sale_amount(item count) using sum and median by day of week.


df_new = parse_date(df.sale_date)
df_new.head()


df['day_of_week'] = df_new['day_of_week']



def aggregate_by_weekday(df):
    return df.groupby('day_of_week')[['sales_total', 'sale_amount']].agg(['median', 'sum'])


# #### Explore the pandas DataFrame.diff() function. Create a new column that is the result of the current sales - the previous days sales.
# 

def add_sales_difference(df):
    df['diff_from_last_day'] = df.sales_total.diff()
    return df


# #### Write a function to set the index to be the datetime variable.

def set_index(df):
    return df.set_index('sale_date', inplace=True)


def prepare_data(df):
    df['sales_total'] = df['sale_amount'] * df['item_price']
    df_new = parse_date(df.sale_date)
    df['year'] = df_new['year']
    df['quarter'] = df_new['quarter']
    df['month'] = df_new['month']
    df['day_of_month'] = df_new['day_of_month']
    df['day_of_week'] = df_new['day_of_week']
    df['is_weekend'] = df_new['is_weekend']
    df = set_index(df)
    df = add_sales_difference(df)
    return df
