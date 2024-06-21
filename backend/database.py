import os
import hvac

# Maak verbinding met Vault
client = hvac.Client(url='http://vault.myolink.info.gf:8200')

# Verifieer met een methode, bijvoorbeeld met een token
client.token = os.getenv('VAULT_TOKEN')  # Zorg dat VAULT_TOKEN is ingesteld in je environment variables

# Lees de database credentials
read_response = client.secrets.kv.read_secret_version(path='/v1/db/data/credentials')
credentials = read_response['data']['data']

username = credentials['username']
password = credentials['password']
host = 'developmentvm1-klasb2c.westeurope.cloudapp.azure.com'  # Corrected the key for host
port = '3306'
database_name = 'db'

# Construct the DATABASE_URL for MariaDB
DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"

# Create the SQLAlchemy engine
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)