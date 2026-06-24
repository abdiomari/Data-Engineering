from dotenv import load_dotenv
from sqlalchemy import create_engine

import os

load_dotenv()

def load(gas_df_clean):

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    USER = os.getenv('USER')
    PORT = os.getenv('PORT')
    DATABASE_PASSWORD =os.getenv('DATABASE_PASSWORD')
    HOST = os.getenv('HOST')


    engine = create_engine(f'postgresql+psycopg2://{USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}')
    gas_df_clean.to_sql('gaspricesv3', engine, if_exists='append', index=False)
