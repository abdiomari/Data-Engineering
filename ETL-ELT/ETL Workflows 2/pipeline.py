import http.client
import pandas as pd
import json
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def extract():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey {NEWS_API_KEY}"
        }

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()
    # data_decoded = data.decode("utf-8")
    # print(res.status_code)
    return data


def transform(data):
    data_staging = json.loads(data)
    result_data = data_staging.get('result')
    cities = result_data.get('cities')

    gas_df = pd.DataFrame(cities)
    gas_df_clean = gas_df.drop(columns="lowername", inplace=True)
    gas_df_clean = gas_df.rename(columns={"name": "cities"}, inplace=True)

    return gas_df

def load(gas_df):

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    USER = os.getenv('USER')
    PORT = os.getenv('PORT')
    DATABASE_PASSWORD =os.getenv('DATABASE_PASSWORD')
    HOST = os.getenv('HOST')


    engine = create_engine(f'postgresql+psycopg2://{USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}')
    gas_df.to_sql('gaspricesv2', engine, if_exists='append', index=False)

def main():
    raw_data = extract()
    transform_data = transform(raw_data)
    load(transform_data)

if __name__ == '__main__':
    main()