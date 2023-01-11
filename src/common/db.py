import os

test_env = 'test'
env = os.environ.get('ENV', test_env)

host = 'localhost' if env == test_env else os.environ['DB_HOST']
user = 'master' if env == test_env else os.environ['DB_USER']
password = 'password' if env == test_env else os.environ['DB_PASS']
name = 'currencies' if env == test_env else os.environ['DB_NAME']

db_uri = f'postgresql://{user}:{password}@{host}/{name}'

print('****\n', db_uri, '***\n')