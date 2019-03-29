import pandas as pd
import env
# the old way:
# def get_db_url(user, pw, host, db):
#     from sqlalchemy import create_engine
#     from env import user, pw, host
#     url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, pw, host, db)
#     return url

# the new way:

def get_connection(db, user=env.user, host=env.host, password=env.pw):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_iris_data():
    return pd.read_sql('SELECT s.species_name, m.* FROM species s JOIN measurements m ON m.species_id = s.species_id', get_connection('iris_db'))

# def get_titanic_data():
#     USER = user
#     PASSWORD = pw
#     HOST = host
#     DATABASE_NAME = 'titanic_db'
#     connection_url = 'mysql+pymysql://USER:PASSWORD@HOST/DATABASE_NAME'
#     sql_query = 'SELECT * FROM titanic_db.passengers;'
#     return pd.read_sql(sql_query, connection_url)


# def get_iris_data():
#     USER = user
#     PASSWORD = pw
#     HOST = host
#     DATABASE_NAME = 'iris_db'
#     sql_query = 'SELECT * FROM iris_db.measurements JOIN iris_db.species USING(species_id);'
#     connection_url = 'mysql+pymysql://USER:PASSWORD@HOST/DATABASE_NAME'
#     iris_df = pd.read_sql(sql_query, connection_url)
#     return iris_df