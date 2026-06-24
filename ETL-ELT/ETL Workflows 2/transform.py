import pandas as pd
import json


def transform(data):
    data_staging = json.loads(data)
    result_data = data_staging.get('result')
    cities = result_data.get('cities')

    gas_df = pd.DataFrame(cities)
    gas_df_clean = gas_df.drop(columns="lowername")
    gas_df_clean = gas_df_clean.rename(columns={"name": "cities"})
    print(f"gas_df: {gas_df.head()}")
    print(f"gas_df_clean: {gas_df_clean.head()}")

    return gas_df_clean