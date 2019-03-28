# JesseRuiz_Codeup_Classification_Exercises_Data Acquisition
# Data Acquisition & Summary

import pandas as pd
from pydataset import data


# # 1. Use the pydataset module to load the iris data set into a dataframe, df_iris

# df = data('iris')
# #     * print the first 3 rows
# print(df.head(3))

# #     * print the number of rows and columns (shape)
# print(df.shape)
# #     * print the column names
# print(df.columns)
# #     * print the data type of each column
# print(df.info())
# print('The data type of the each column is: ', [df.columns.dtype for col in df.columns])

# #     * print the summary statistics for each of the numeric variables. 
# for element in ['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']:
#     print(df[[element]].describe())

# # Would you recommend rescaling the data based on these statistics?
# # No. But yes if we were going to use this in a regression model.


# # 2. Read the data tab from the stats module dataset, Excel_Stats.xlsx, into a dataframe, df_excel


# path = '~/Documents/Coding/Codeup/CourseWork/'
# file = 'Jesse Ruiz - Excel_Stats.xlsx'
# df_excel = pd.read_excel(path+file,sheet_name="data_ex3")

# #     * assign the first 100 rows to a new dataframe, df_excel_sample
# df_excel_sample = df_excel.sample(100)

# #     * print the number of rows of your original dataframe
# print(df_excel.shape)
# #     * print the first 5 column names
# print('The first 5 columns: ',df_excel.columns[0:5])
# #     * print the column names that have a data type of object
# object_cols = []
# for col in df_excel.columns:
#     if df_excel[col].dtype == 'object':
#         object_cols.append(col)
# print('The object columns:',object_cols)

# # ALSO: 
# print('This is the alternative method: ',df_excel.select_dtypes(include=['object']).columns)

# #     * compute the range for each of the numeric variables.
# numeric_cols = []
# for col in df_excel.columns:
#     if df_excel[col].dtype == 'int64':
#         numeric_cols.append(col)
# print(numeric_cols)

# for col in numeric_cols:
#     print('The range of',col, 'is ',(df_excel[col].max() - df_excel[col].min()))


# print(df_excel['tenure'].max() - df_excel['tenure'].min())

# # 3. Read train.csv from google drive (shared through classroom in topic 'Classification') into a dataframe labeled df_google
# df_google = pd.read_clipboard()
# # pd.read_csv('https://docs.google.com/spreadsheets/d/1hc435tBI6Zn0OFxjhVIsmWwj2Ri21SjaikpXDd5g1rU/export?format=csv#gid=451332569', usecols=range(0,7), header=0)


# #     * print the first 3 rows
# print(df_google.head(3))

# #     * print the number of rows and columns
# print(df_google.shape)

# #     * print the column names
# print(df_google.columns)
# print('------------')

# #     * print the data type of each column
# for col in df_google.columns:
#     print('The column data type is ',df_google[col].dtype,'for ',col)

# #     * print the summary statistics for each of the numeric variables
# numeric_cols = []
# for col in df_google.columns:
#     if df_google[col].dtype == 'int64':
#         numeric_cols.append(col)

# for col in numeric_cols:
#     print(df_google[col].describe())

# #     * print the unique values for each of your categorical variables

# object_cols = []
# for col in df_google.columns:
#     if df_google[col].dtype == 'object':
#         object_cols.append(col)

# for col in object_cols:
#     print(df_google[col].unique())


# # 4. In mysql workbench or a terminal, write a query to select all the columns of the passengers table from the titanic database. 
# # Export that table to a csv you store locally. Read that csv into a dataframe df_csv.

path = '~/Documents/Coding/Codeup/CourseWork/Classification/'
file = 'titanic.csv'
df_csv = pd.read_csv(path+file)


#     * print the head and tail of your new dataframe
print(df_csv.head())
print(df_csv.tail())

#     * print the number of rows and columns
print('the number of rows and columns')
print(df_csv.shape)

#     * print the column names
print('the column names')
print(df_csv.columns)

#     * print the data type of each column
print('the data type of each column')
for col in df_csv.columns:
    print(df_csv[col].dtype)

#     * print the summary statistics for each numeric variable
print('the summary statistics for each numeric variable')
numeric_cols = []
for col in df_csv.columns:
    if df_csv[col].dtype == 'int64':
        numeric_cols.append(col)

for col in numeric_cols:
    print(df_csv[col].describe())

#     * print the unique values for each categorical variables. 
# If there are more than 5 distince values, print the top 5 in terms of prevelence or frequency.

object_cols = []
for col in df_csv.columns:
    if df_csv[col].dtype == 'object':
        object_cols.append(col)

for col in object_cols:
    print('the unique values for each categorical variable in',col,'are:', df_csv[col].unique()[:5])

