from pymongo import MongoClient


class Database:
    URI = "mongodb://localhost:27017/ppnwates"
    DATABASE = MongoClient(URI).get_database()

    @staticmethod
    def insert_one(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_last_login(collection, query, data):
        Database.DATABASE[collection].update_one(query, {"$set": data}, upsert=True)

    @staticmethod
    def update_one_data(collection, query, data):
        Database.DATABASE[collection].update_one(query, {"$set": data}, upsert=True)

    @staticmethod
    def find(collection, data):
        return Database.DATABASE[collection].find(data)

# db.mycollection.find({
#     "someArray.someNestedArray.name": "value"
# })
