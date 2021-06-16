import json
from tqdm import tqdm
from getpass import getpass
import configparser
from help_function.connect_services_aws import getAccessFromS3
from help_function.connect_rds_mysql import connect_mysql
from help_function.remove_keys_and_values import remove_keys_and_values

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['S3']

## Criando variavel da SDK do S3
s3 = getAccessFromS3()

print(" --- > Leitura do arquivo do bucket")# Leitura do arquivo do bucket
obj = s3.Bucket(credentials['bucket_name']).Object('countries.json').get()

# Capturar os dados do json
# with open('countries.json', 'r') as file:
#     countries = json.load(file)

countries = json.load(obj['Body'])

print(" --- > Inicializando o conexão com a base de dados")
db = connect_mysql()
cursor = db.cursor()
my_data = []

print(" --- > Inserindo dados no banco")
for i in tqdm(countries):
    my_dic = remove_keys_and_values(i)
    country = str(my_dic['Country']).replace("'"," ")
    slug = my_dic['Slug']
    cod_country = my_dic['ISO2']
    cursor.execute(f"INSERT INTO Countries (country_name,slug,country_code) VALUES ('{country}','{slug}','{cod_country}');")
    db.commit()

print(" --- > Processo finalizado!")
cursor.close()