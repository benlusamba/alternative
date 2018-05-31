# Automated news retrieval using newsapi.org (or other API of your choosing)

import pandas as pd
import numpy as np
import urllib.request
import os
import csv
import requests
import json
import json as simplejson
import common

print('^ Word Frequency Count')

# define parameters, including API KEY

params = (
    ('q', 'nafta,trump,deal,tariff'),
    ('apiKey', 'e76a07388cad49b49075abced2862f3d'),
)

response = requests.get('https://newsapi.org/v2/everything', params=params)

data = response.json()

# write response as JSON file to enable parsing
f = open('nafta.json', 'w')
simplejson.dump(data, f)
f.close()

#parse JSON file using pandas
data = pd.read_json('nafta.json', lines=True)

df_json_raw = pd.read_json('nafta.json')

# Add variables as desired e.g. 'source'


df_json = df_json_raw.apply( lambda x: pd.Series([x[2]['description'],x[2]['title'],x[2]['publishedAt']]), axis = 1)

# Label columns for csv file
#df_json.columns=['Title','Description','Published At','Source']
df_json.columns=['Description', 'Title', 'Published At']

#export as csv
df_json.to_csv('nafta.csv')
