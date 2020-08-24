# from dataclasses import dataclass, field
from typing import List, Dict
import uuid

from common.database import Database
from model.item import Item
from model.user.user import User
from model.model import Model


# @dataclass(eq=False)  # can delete and change to the normal format
class Alert(Model):

    collection = "alerts"
#    collection: str = field(init=False, default="alerts")
#    name: str
#    item_id: str
#    price_limit: float
#    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __init__(self, name: str, item_id: str, price_limit: float, user_email: str, _id: str = None):
        super().__init__()
        self.name = name
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.user_email = user_email
        self._id = _id or uuid.uuid4().hex
        self.user = User.find_by_email(user_email)

#    def __post_init__(self):
#        self.item = Item.get_by_id(self.item_id)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "item_id": self.item_id,
            "price_limit": self.price_limit,
            "user_email": self.user_email
        }

#    def save_to_mongo(self):
#        Database.insert(self.collection, self.json())

    def load_item_price(self) -> float:
        price = self.item.load_price()
        return price  # self.item.price

    def notify_if_price_reached(self):
        if self.item.price <= self.price_limit:
            print(f"Item {self.item} has reached the price under {self.price_limit}. The price: {self.item.price}")

#    @classmethod
#    def all(cls) -> List:
#        alerts_from_db = Database.find(cls.collection, {})
#        return [cls(**alert) for alert in alerts_from_db]
