import mysql
import mysql.connector
from getpass import getpass
import configparser 

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['RDS']

def connect_mysql():
    '''MySQL connection located in RDS.'''
    try:
        db = mysql.connector.connect(
            host=credentials['host'],
            user=credentials['user'],
            password=credentials['password'],
            database=credentials['database']
        )

        return db
    except:
        return Exception("Não foi possível conectar a base")

    
    
