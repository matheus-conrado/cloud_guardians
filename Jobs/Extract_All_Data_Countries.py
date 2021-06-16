from datetime import datetime, date
import requests
import json
from tqdm import tqdm
from help_function.connect_services_aws import getAccessFromS3
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['S3']

## Criando variavel da SDK do S3
s3 = getAccessFromS3()

print(" --- > Efetuando leitura dos dados para busca de casos")
obj = s3.Bucket(credentials['bucket_name']).Object('countries.json').get()

#Colentando os dados de retorno do S3
countries = json.load(obj['Body'])

data = {}

print(" --- > Efetuando leitura dos dados")
for country in tqdm(countries):
  url = f"https://api.covid19api.com/country/{country['Slug']}?from=2020-01-22T00:00:00Z&to={datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')}"
  response = requests.request("GET", url, headers={}, data={})
  d = response.json()
  data[country['Country']] = list(d)

new_data = []
for i in data:
  new_data = new_data + data[i]

with open('data_all_countries.json', 'w') as file:
  json.dump(new_data, file)

print(" --- > Gravando dados no S3")
s3.Bucket(credentials['bucket_name']).upload_file(Filename='data_all_countries.json', Key='data_all_countries.json')