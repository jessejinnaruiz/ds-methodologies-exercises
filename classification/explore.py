# Data Exploration
import numpy as np
import pandas as pd

from numpy.random import randn

# Modeling
import statsmodels.api as sm
import scipy.stats as stats

from scipy.stats import pearsonr

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, median_absolute_error

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# %matplotlib inline

import math

from sklearn.linear_model import LinearRegression

from sklearn import metrics

import statsmodels.api as sm

from pprint import pprint

# get data
from acquire import get_iris_data
df = get_iris_data()

# Split data into train (70%) & test (30%) samples. You should end with 2 data frames: train_df and test_df
train_df, test_df = train_test_split(df, test_size=.30, random_state=123)

# Create a swarmplot where the x-axis is each of the independent variable names (petal_length, petal_width, etc). The y-axis is the value of the variable. Use color to represent species as another dimension. Hint: You will to 'melt' the dataframe into a 'long' dataframe in order to accomplish this. What are your takeaways from this visualization?
# THE VIRGINICA SPECIES HAS LARGER MEASUREMENTS OVERALL EXCEPT FOR SEPAL WIDTH
# THE SETOSA SPECIES HAS LOWER MEASUREMENTS OVERALL EXCEPT FOR THE SEPAL WIDTH, WHICH IS THE HIGHEST COMPARED TO OTHER SPECIES.
train_df.head()

df_melted = pd.melt(train_df, id_vars=['species_name'], value_vars=('sepal_length','sepal_width','petal_length','petal_width'), var_name='measurement in cm')
df_melted.head()


plt.figure(figsize=(12,12))
sns.swarmplot(x="measurement in cm", y='value', data=df_melted, hue="species_name")


# Create 4 subplots (2 rows x 2 columns) of scatterplots


# sepal_length x sepal_width
# petal_length x petal_width
# sepal_area x petal_area
# sepal_length x petal_length

# Make your figure size 14 x 8. What are your takeaways?
# PETAL LENGTH AND WIDTH ARE CORRELATED STRONGLY.
# PETAL LENGTH AND SEPAL LENGTH ARE CORRELATED STRONGLY.
# PETAL AREA AND SEPAL AREA ARE CORRELATED WEAKLY.

fig = plt.figure(figsize=(14,8))

plt.subplot(2, 2, 1)
sns.scatterplot(x='sepal_length', y='sepal_width', data=train_df)

plt.subplot(2, 2, 2)
sns.scatterplot(x='petal_length', y='petal_width', data=train_df)

plt.subplot(2, 2, 3)
sns.scatterplot(x='sepal_area', y='petal_area', data=train_df)

plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal_length', y='petal_length', data=train_df)

plt.show()

# Create a heatmap of each variable layering correlation coefficient on top.
sns.heatmap(train_df.drop(columns=['measurement_id','species_id']).corr(), cmap='YlOrBr', annot=True)

# Create a scatter matrix visualizing the interaction of each variable
from pandas.tools.plotting import scatter_matrix
from matplotlib import cm

cmap = cm.get_cmap('gnuplot')
scatter = pd.scatter_matrix(
    train_df.drop(columns=['measurement_id','species_id']), marker='o', s=40,
    hist_kwds={'bins':15},  figsize=(9,9), cmap=cmap)

# Is the sepal length significantly different in virginica than versicolor? Run an experiment to test this.

# must include null hypothesis, alternative hyp, t-test, results, summary
# H0: the difference in sepal length between virginica and versicolor is insignificant.
# Ha: the difference in sepal length between virginica and versicolor is substantial.
# We will test if the sepal length of virginica is significantly different than that of the versicolor.
# If there is difference, then variable sepal_length is a good choice to keep as a feature.
# We can use a t-test here, as sepal_length is somwhat normally distributed.
import scipy as sp 
import numpy as np

sp.stats.ttest_ind(veri['sepal_length'],virg['sepal_length'])
# The t-test results show that the p-value is very close to 0, which means it is reliable. 
# The t-stat is -4.3 meaning the difference is 4.3X different. 
# The value sepal_length between two different species, Versicolor and Virginica.