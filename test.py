import pandas as pd
import requests

url = "https://catalog.ourworldindata.org/garden/covid/latest/cases_deaths/cases_deaths.csv"
csv_path = "/tmp/covid.csv"

r = requests.get(url)
with open(csv_path, 'wb') as fin:
    fin.write(r.content)

df = pd.read_csv(csv_path)
print(df.head())
print(df.tail())
print(df.columns)
