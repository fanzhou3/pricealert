from typing import Dict, List
from model.item import Item
import uuid
from common.database import Database
from model.model import Model
#from dataclasses import dataclass, field


#@dataclass(eq=False)  # can delete and change to the normal format
class Alert(Model):

    collection = "alerts"
#    collection: str = field(init=False, default="alerts")
#    name: str
#    item_id: str
#    price_limit: float
#    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __init__(self, name: str, item_id: str, price_limit: float, _id: str = None):
        super().__init__()
        self.name = name
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = _id or uuid.uuid4().hex

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
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
