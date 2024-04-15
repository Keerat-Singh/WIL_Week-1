# from pymongo import MongoClient
from pymongo.mongo_client import MongoClient

def get_database():
   cluster = MongoClient("mongodb+srv://new_user_1:new_user_1@autobasket.rbhfxd5.mongodb.net/?retryWrites=true&w=majority&appName=AutoBasket")
   db = cluster['Autobasket']
   collection = db['User']
   return db

get_database()