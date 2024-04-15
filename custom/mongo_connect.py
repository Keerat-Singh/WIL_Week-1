from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



def mongo_ping():
    # Replace the placeholder with your Atlas connection string
    uri = "mongodb://localhost:27017/"
    # Set the Stable API version when creating a new client
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def mongo_table(table_name):
    try:
        # Replace the placeholder with your Atlas connection string
        uri = "mongodb://localhost:27017/"
        # Set the Stable API version when creating a new client
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["AutoBasket"]
        collection = db[table_name]
        user_data = {"User ID":15250,"User Name":"Brandon Campbel",
                    "User Email":"brandom.campbel@gmail.com",
                    "Password" : "brandon.campbel",
                    "User Age":30,"Weekly Shopping Budget":100,
                    "Dietary Preferences":"Egg Allergy"}
        user_mongo_id = collection.insert_one(user_data).inserted_id
        return user_mongo_id
    except Exception as e:
        print(e)
        return e