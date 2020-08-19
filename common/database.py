from typing import Dict
import pymongo


class Database:
    URL = "mongodb://127.0.0.1:27017/pricealert"
    DATABASE = pymongo.MongoClient(URL).get_database()

    @staticmethod
    def insert( collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)