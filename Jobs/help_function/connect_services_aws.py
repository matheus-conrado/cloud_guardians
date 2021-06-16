import boto3
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['boto3']

def getAccessFromS3():
    '''S3 connection located in AWS.'''
    try:
        s3 = boto3.resource(
            service_name= credentials['service_name'],
            region_name=credentials['region_name'],
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key']
        )
        return s3
    except:
        return Exception("Não foi possivel conectar a estrutura do S3")