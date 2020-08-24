from typing import Dict
import pymongo
import os


class Database:
    URL = "mongodb://dezhong:dezhong3@ds133922.mlab.com:33922/heroku_vcf86tkr"
    #  URL =  "mongodb://127.0.0.1:27017/pricealert"
    DATABASE = pymongo.MongoClient(URL).get_default_database()    # get_database()

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