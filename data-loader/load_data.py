import pandas as pd
import requests
from sqlalchemy import create_engine
import time
import os

# Stand up PostgreSQL environment variables and connection
db_host = os.getenv('DB_HOST', 'db')
db_user = os.getenv('DB_USER', 'covid')
db_pass = os.getenv('DB_PASS', 'covid')
db_name = os.getenv('DB_NAME', 'covid_data')

engine = None
while engine is None:
    try:
        engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}')
        engine.connect()
    except Exception as e:
        print('Waiting for PostgreSQL to be ready...')
        time.sleep(3)

url = "https://catalog.ourworldindata.org/garden/covid/latest/cases_deaths/cases_deaths.csv"
csv_path = "/tmp/covid.csv"

r = requests.get(url)
with open(csv_path, 'wb') as fin:
    fin.write(r.content)

df = pd.read_csv(csv_path)
df.to_sql('covid_data', engine, if_exists='replace', index=False)
print('Data loaded successfully!')
