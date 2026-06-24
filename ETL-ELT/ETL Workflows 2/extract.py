import http.client
import os

def extract():
    conn = http.client.HTTPSConnection("api.collectapi.com")
    # NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 7pHa2riXv8zVFg2vqLTwFW:5ykIpDOwail5fPmF5tLRLQ"
        }

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()
    # data_decoded = data.decode("utf-8")
    # print(res.status_code)
    return data
