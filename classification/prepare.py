import pandas as pd

# 1. Iris Data
# Use the function defined in acquire.py to load the iris data.
from acquire import get_iris_data
# print(get_iris_data())
# a. Drop the species_id and measurement_id columns.
iris_df = get_iris_data()
iris_df = iris_df.drop(['species_id','measurement_id'], axis=1)
# b. Rename the species_name column to just species.
iris_df = iris_df.rename(columns={'species_name': 'species'})
# print(iris_df)
# c. Encode the species name using a sklearn label encoder. 
# Research the inverse_transform method of the label encoder. How might this be useful?
from sklearn import preprocessing
encoder = preprocessing.LabelEncoder()
encoder.fit(iris_df.species)
iris_df.species = (encoder.transform(iris_df.species))
# print('after encoder...')
# print(iris_df)


# Create a function named prep_iris that accepts the untransformed iris data, 
# and returns the data with the transformations above applied.
def drop_columns(iris_df):
    return iris_df.drop(['species_id','measurement_id'], axis=1)

def rename_columns(iris_df):
    return iris_df.rename(columns={'species_name': 'species'})

def encode_species_col(iris_df):
    from sklearn import preprocessing
    encoder = preprocessing.LabelEncoder()
    encoder.fit(iris_df.species)
    return iris_df.assign(species_encode = encoder.transform(iris_df.species))

def prep_iris(iris_df):
    return iris_df.pipe(drop_columns)\
        .pipe(rename_columns)\
        .pipe(encode_species_col)

# 2. Titanic Data
# Use the function you defined in acquire.py to load the titanic data set.
from acquire import get_titanic_data
titanic_df = get_titanic_data()
# print(titanic_df)
# Write the code to perform the operations below. (Do this yourself, don't copy from the curriculum.)

# a. Handle the missing values in the embark_town and embarked columns.
# print(titanic_df['embark_town'].unique())
titanic_df.embark_town.fillna(value='Unknown', inplace=True)
# print(titanic_df)
# print(titanic_df['embarked'].unique())
titanic_df.embarked.fillna(value='Unknown', inplace=True)


# b. Remove the deck column.
titanic_df = titanic_df.drop(['deck'], axis=1)
# print(titanic_df)

# c. Use a label encoder to transform the embarked column.
from sklearn import preprocessing
encoder = preprocessing.LabelEncoder()
encoder.fit(titanic_df.embarked)
titanic_df.embarked = (encoder.transform(titanic_df.embarked))
# print('after encoder...')
# print(titanic_df.embarked)

# d. Scale the age and fare columns using a min max scaler. 
# Why might this be beneficial? When might you not want to do this?
# FOR WHEN WE WANT TO COMPARE VARIABLES ON A SIMILAR SCALE

# --------OMITTED FROM EXERCISE---------

# Create a function named prep_titanic that accepts the untransformed titanic data, and returns the data with the transformations above applied.

def handle_missing(titanic_df):
    return titanic_df.assign(embarked=titanic_df.embarked.fillna(value='0'), embarked_town=titanic_df.embark_town.fillna(value='Other'))

def remove_columns(titanic_df):
    return titanic_df.drop(columns=['deck'])

def encode_embarked_col(titanic_df):
    from sklearn import preprocessing
    encoder = preprocessing.LabelEncoder()
    encoder.fit(titanic_df.embarked)
    return titanic_df.assign(embarked_encode = (encoder.transform(titanic_df.embarked)))

def prep_titanic(titanic_df):
    titanic_df = titanic_df.pipe(handle_missing).pipe(remove_columns).pipe(encode_embarked_col)
    return titanic_df


# 3. Save your prep_titanic and prep_iris functions in a file named prepare.py so that we can use them later on.

