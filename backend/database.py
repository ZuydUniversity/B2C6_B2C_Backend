import hvac

# Initialize the Vault client
client = hvac.Client(url='http://vault.myolink.info.gf:8200')

def login_with_userpass(username, password):
    """
    Log in to Vault using the Username (userpass) method and set the client token.
    """
    try:
        # Authenticate with Vault using the userpass method
        login_response = client.auth.userpass.login(
            username=username,
            password=password,
            mount_point='userpass'
        )
        
        # Set the client token to the newly acquired token
        client.token = login_response['auth']['client_token']
    except Exception as e:
        print(f"Error logging in to Vault: {e}")
        return "null"
    return login_response['auth']['client_token']

# Use the function with your credentials

try:
    token = login_with_userpass("databaseuser", "nzF2Y0Pa1xImII5M3vzkDM")
    client.token = token
    print(client.token)
    secrets_engines_list = client.sys.list_mounted_secrets_engines()['data']
    print('The following secrets engines are mounted: %s' % ', '.join(sorted(secrets_engines_list.keys())))
    # Now you can proceed with the rest of your script, using the authenticated client
    # Read the database credentials
    read_response = client.secrets.kv.v2.create_or_update_secret(path='db/test', secret=dict(pssst="this is a secret"))
    credentials = read_response['data']['data']

    password = credentials['password']
    username = credentials['username']
    host = 'developmentvm1-klasb2c.westeurope.cloudapp.azure.com'
    port = '3306'
    database_name = 'myolinkdb'

    # Construct the DATABASE_URL for MariaDB
    database_url = f"mariadb://{username}:{password}@{host}:{port}/{database_name}"
    print(database_url)
except Exception as e:
    print(f"Error reading secret: {e}")