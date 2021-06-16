from datetime import datetime, date
import requests
import boto3
import json
from tqdm import tqdm
from help_function.connect_services_aws import getAccessFromS3
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['S3']

## Criando variavel da SDK do S3
s3 = getAccessFromS3()

url = 'https://api.covid19api.com/countries'

countries = requests.request("GET", url, headers={}, data={})

with open('countries.json', 'w') as file:
    json.dump(countries.json(), file)

s3.Bucket(credentials['bucket_name']).upload_file(Filename='countries.json', Key='countries.json')