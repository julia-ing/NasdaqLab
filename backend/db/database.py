from pymongo import MongoClient

client = MongoClient(f'mongodb://127.0.0.1:27017')
DB_NAME = "ccde"
db = client[DB_NAME]