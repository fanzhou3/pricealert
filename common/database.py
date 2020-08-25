from typing import Dict
import pymongo
import os


class Database:
    #  URL = "mongodb+srv://dezhong:<password>@cluster0.2tfzy.mongodb.net/<dbname>?retryWrites=true&w=majority"
    #  URL =  "mongodb://127.0.0.1:27017/pricealert"

    client = pymongo.MongoClient(
        "mongodb+srv://dezhong:sdz7838303@cluster0.2tfzy.mongodb.net/price_alert?retryWrites=true&w=majority")
    # db = client.test

    DATABASE = client.get_database()    # get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)

    @staticmethod
    def initialize():
        return Database.DATABASE["test"].name
