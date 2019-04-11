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

def get_mall_data():
    return pd.read_sql('SELECT * FROM customers', get_connection('mall_customers'))

