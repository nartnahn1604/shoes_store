from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")
conn = MongoClient(config.get("DATABASE_CONNECTION_URL"))
db = conn.dddstore
collection = db.shoes