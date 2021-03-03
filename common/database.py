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