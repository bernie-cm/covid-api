import pandas as pd

url = "https://catalog.ourworldindata.org/garden/covid/latest/cases_deaths/cases_deaths.csv"

df = pd.read_csv(url)
print(df.head())
print(df.tail())
print(df.columns)