from pymongo import MongoClient
from utils import env_config

# connection with MongoDB client.
client = MongoClient(env_config.DATABASE_SERVER_HOST)
db = client[env_config.DATABASE_NAME]
collection = db[env_config.COLLECTION_NAME]
id_counter_collection = db[env_config.ID_COUNTER_NAME]