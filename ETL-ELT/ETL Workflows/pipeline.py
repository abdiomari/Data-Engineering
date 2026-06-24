import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
USER = os.getenv('USER')
PORT = os.getenv('PORT')
DATABASE_PASSWORD =os.getenv('DATABASE_PASSWORD')
HOST = os.getenv('HOST')


def extract_data():
    url = 'https://newsapi.org/v2/everything?q=apple&from=2026-06-09&to=2026-06-09&sortBy=popularity&apiKey=2bf6f6301f924a82b621b3aec134747f'

    res = requests.get(url)
    data = res.json()
    print(res.status_code)

    return data


def transform_data(data):
    articles = data.get('articles')
    articles_df = pd.DataFrame(articles)
    articles_df.head()
    try:
        articles_df.drop(columns=['source', 'urlToImage'], inplace=True)
    except KeyError as e:
        print(f'Raised Key Error: {e}')

    return articles_df


def load_data(articles_df):

    engine = create_engine(f'postgresql+psycopg2://{USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}')
    articles_df.to_sql('articlesv2', engine, if_exists='append', index=False)

    message= "pipeline run successful"
    return message

def run_pipeline():
    raw_data = extract_data()
    clean_data_as_df = transform_data(raw_data)
    load_clean_data = load_data(clean_data_as_df)

    print(load_clean_data)

run_pipeline()