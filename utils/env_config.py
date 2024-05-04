import os
from dotenv import load_dotenv

load_dotenv()

SERVER_PORT = os.environ.get('SERVER_PORT')
SERVER_HOST = os.environ.get('SERVER_HOST')
DATABASE_SERVER_HOST = os.environ.get('DATABASE_SERVER_HOST')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
ID_COUNTER_NAME = os.environ.get('ID_COUNTER_NAME')