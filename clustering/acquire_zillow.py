import pandas as pd
import env


def get_connection(db, user=env.user, host=env.host, password=env.pw):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_data_2016():
    return pd.read_sql('SELECT * FROM zillow.properties_2016\
        LEFT JOIN airconditioningtype ON properties_2016.airconditioningtypeid = airconditioningtype.airconditioningtypeid\
            LEFT JOIN architecturalstyletype ON properties_2016.architecturalstyletypeid = architecturalstyletype.architecturalstyletypeid\
                LEFT JOIN buildingclasstype ON properties_2016.buildingclasstypeid = buildingclasstype.buildingclasstypeid\
                    LEFT JOIN heatingorsystemtype ON properties_2016.heatingorsystemtypeid = heatingorsystemtype.heatingorsystemtypeid\
                        LEFT JOIN propertylandusetype ON properties_2016.propertylandusetypeid = propertylandusetype.propertylandusetypeid\
                            LEFT JOIN storytype ON properties_2016.storytypeid = storytype.storytypeid\
                                LEFT JOIN typeconstructiontype ON properties_2016.typeconstructiontypeid = typeconstructiontype.typeconstructiontypeid\
                                    LEFT JOIN predictions_2016 ON properties_2016.parcelid = predictions_2016.parcelid;', get_connection('zillow'))

def save_df_2016():
    df_2016 = get_zillow_data_2016()
    df_2016.to_csv('2016_Zillow_Data.csv')

def get_zillow_data_2017():
    return pd.read_sql('SELECT * FROM zillow.properties_2017\
        LEFT JOIN airconditioningtype ON properties_2017.airconditioningtypeid = airconditioningtype.airconditioningtypeid\
            LEFT JOIN architecturalstyletype ON properties_2017.architecturalstyletypeid = architecturalstyletype.architecturalstyletypeid\
                LEFT JOIN buildingclasstype ON properties_2017.buildingclasstypeid = buildingclasstype.buildingclasstypeid\
                    LEFT JOIN heatingorsystemtype ON properties_2017.heatingorsystemtypeid = heatingorsystemtype.heatingorsystemtypeid\
                        LEFT JOIN propertylandusetype ON properties_2017.propertylandusetypeid = propertylandusetype.propertylandusetypeid\
                            LEFT JOIN storytype ON properties_2017.storytypeid = storytype.storytypeid\
                                LEFT JOIN typeconstructiontype ON properties_2017.typeconstructiontypeid = typeconstructiontype.typeconstructiontypeid\
                                    LEFT JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid;', get_connection('zillow'))

def save_df_2017():
    df_2017 = get_zillow_data_2017()
    df_2017.to_csv('2017_Zillow_Data.csv')