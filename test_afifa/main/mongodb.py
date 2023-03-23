from pymongo import MongoClient
from test_afifa.settings import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

users = db['users']
users.create_index('id', unique=True)
