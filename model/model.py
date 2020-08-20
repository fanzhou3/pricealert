from abc import ABCMeta, abstractmethod
from typing import Dict, List, TypeVar, Type
from common.database import Database

T = TypeVar('T', bound='Model')  # T must be a 'Model' or a subclass of 'Model'


class Model(metaclass=ABCMeta):

    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:  # Item.get_by_id() -> Item, Alert.get_by_id() -> Alert
        return cls.find_by_one("_id", _id)

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_by_one(cls: Type[T], attribute: str, value: str) -> T:
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
