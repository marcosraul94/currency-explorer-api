import os

host = os.environ.get('DB_HOST', 'localhost')
user = os.environ.get('DB_USER', 'admin')
password = os.environ.get('DB_PASS', 'password')
name = os.environ.get('DB_NAME', 'currency-explorer')

db_uri = f'postgresql://{user}:{password}@{host}/{name}'
