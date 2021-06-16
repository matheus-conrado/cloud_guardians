import json
from tqdm import tqdm
from datetime import datetime
import configparser
from help_function.connect_services_aws import getAccessFromS3
from help_function.connect_rds_mysql import connect_mysql
from help_function.remove_keys_and_values import remove_keys_and_values

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['S3']

## Criando variavel da SDK do S3
s3 = getAccessFromS3()

entries = ('ID','CountryCode','Province','City','CityCode')

values = []

# Leitura do arquivo do bucket
print("Leitura do arquivo do bucket")
obj = s3.Bucket(credentials['bucket_name']).Object('data_all_countries.json').get()

data_all_countries = json.load(obj['Body'])

db = connect_mysql()

cursor = db.cursor()

print(" --- > Preparando os dados para inserção")

for i in tqdm(range(len(data_all_countries))):
    final = []
    final.append(data_all_countries[i]['Country'])
    final.append(float(data_all_countries[i]['Lat']))
    final.append(float(data_all_countries[i]['Lon']))
    final.append(int(data_all_countries[i]['Confirmed']))
    final.append(int(data_all_countries[i]['Deaths']))
    final.append(int(data_all_countries[i]['Recovered']))
    final.append(int(data_all_countries[i]['Active']))
    final.append(str(data_all_countries[i]['Date'])[:10])
    final = tuple(final)
    values.append(final)

query = """INSERT INTO Cases_covid (country_name,lat,lon,confirmed,deaths,recovered,active,date_register) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

print(" --- > Inserindo dados no banco")
cursor.executemany(query,values)
db.commit()


print(" --- > Processo finalizado!")
cursor.close()
