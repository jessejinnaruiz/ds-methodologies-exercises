#!/usr/bin/env python
# coding: utf-8
#JesseRuiz_Codeup_tsa_exercises_2019


import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt

from acquire import get_all_data



test_dates = pd.DataFrame(data={'date': ['08/08/88','08/09/1988','08-10-1988','08-11-1988'],'extra':['','','','']})
test_dates



# df = get_all_data()


# ####  Write a function to convert a date to a datetime data type.
# 

def convert_to_datetime(date):
    return pd.to_datetime(date, format = "%m/%d/%y", infer_datetime_format=True)


# convert_to_datetime('08/08/88')

# pd.to_datetime(test_dates['date'])


# #### Write a function to change a datetime to UTC.

def convert_to_utc(date):
    return convert_to_datetime(date).utcnow()

# convert_to_utc('08-08-88')




# #### Write a function to parse a date column into 6 additional columns (while keeping the original date): year, quarter, month, day of month, day of week, weekend vs. weekday


def parse_date(date):
    new_date = pd.to_datetime(date)
    return pd.DataFrame(data={'date_original': new_date,'year': new_date.dt.year, 'quarter': new_date.dt.quarter, 'month': new_date.dt.month,'day_of_month': new_date.dt.day, 'day_of_week': new_date.dt.weekday_name})

# parse_date(test_dates['date'])


# #### Add a column to your dataframe, sales_total, which is a derived from sale_amount (total items) and item_price.

# df.groupby('sale_id').tail(20)


# for col in df.columns:
#     print(col,':', df[col].dtype)

# df['sales_total'] = df['sale_amount'] * df['item_price']

# df.head()


# #### Create a new dataframe that aggregates the sales_total and sale_amount(item count) using sum and median by day of week.

# df_new = parse_date(df.sale_date)
# df_new.head()

# df['day_of_week'] = df_new['day_of_week']

# df.head()

# df_agg_sum = df[['sales_total','sale_amount','day_of_week']].groupby('day_of_week').sum()
# df_agg_sum = df_agg_sum.rename(index=str, columns={'sales_total': 'sum_sales_total', 'sale_amount': 'sum_sale_amount'})
# df_agg_sum

# df_agg_med = df[['sales_total','sale_amount','day_of_week']].groupby('day_of_week').median()
# df_agg_med = df_agg_med.rename(index=str, columns={'sales_total': 'median_sales_total', 'sale_amount': 'median_sale_amount'})
# df_agg_med


# df_agg = pd.concat([df_agg_sum, df_agg_med], axis = 1)
# df_agg


# #### Explore the pandas DataFrame.diff() function. Create a new column that is the result of the current sales - the previous days sales.
# 

# df.tail(10)

# df = df.drop(columns=['cum_sales','cum_sales_by_date'])

# df.head()

# df['diff_total_sales'] = df.sales_total.diff()

# df.head(10)


# #### Write a function to set the index to be the datetime variable.

# def set_index(df):
#     return df.set_index('sale_date', inplace=True)

# set_index(df)

# df.head()


