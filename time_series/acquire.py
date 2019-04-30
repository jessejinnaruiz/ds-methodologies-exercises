"""Acquire script for Time Series Analysis Module
Jesse Jinna Ruiz
2019
"""

import pandas as pd
import numpy as np
from datetime import datetime
import itertools

# JSON API
import requests
import json

# data visualization
import matplotlib
import seaborn as sns
import statsmodels.api as sm

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

base_url = 'https://python.zach.lol'


# ### Get items

def get_items():
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    items = pd.DataFrame(data['payload']['items'])
    page = '/api/v1/items?page='
    number = 2
#     print(data)
    for i in range(data['payload']['max_page']-1):        
        page_number = page+str(number+i)
#         print(page_number)
        response = requests.get(base_url + page_number)
        data=response.json()
        items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index(drop=True)
#         print(items)
    return items

# items = get_items()


# ### Get stores

def get_stores():
    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    page = '/api/v1/items?page='
    number = 2
    for i in range(data['payload']['max_page']-1):
        page_number = page+str(number+i)
        response = requests.get(base_url + page_number)
        data=response.json()
        stores = pd.concat([stores, pd.DataFrame(data['payload']['stores'])]).reset_index(drop=True)
    return stores

# stores = get_stores()


# ### Get sales

def get_items():
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    items = pd.DataFrame(data['payload']['items'])
    page = '/api/v1/items?page='
    number = 2
#     print(data)
    for i in range(data['payload']['max_page']-1):        
        page_number = page+str(number+i)
#         print(page_number)
        response = requests.get(base_url + page_number)
        data=response.json()
        items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index(drop=True)
#         print(items)
    return items



def get_sales():
    response = requests.get('https://python.zach.lol/api/v1/sales')
    data = response.json()
    sales = pd.DataFrame(data['payload']['sales'])
    page = '/api/v1/items?page='
    number = 2
    for i in range(data['payload']['max_page']-1):
        page_number = page+str(number+i)
        response = requests.get(base_url + data['payload']['next_page'])
        data=response.json()
        sales = pd.concat([sales, pd.DataFrame(data['payload']['sales'])]).reset_index(drop=True)
    return sales




# sales = get_sales()


# ### Concatenate dataframes

def get_all_data():
    sales = get_sales()
    stores = get_stores()
    items = get_items()

    sales.rename(columns={'store': 'store_id', 'item': 'item_id'}, inplace=True)
    df = pd.merge(sales, items, on='item_id')
    df = pd.merge(df, stores, on='store_id')

    return df

# sales_df = get_all_data()
# sales_df.to_csv('sales_df.csv')




