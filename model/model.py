from abc import ABCMeta, abstractmethod
from typing import Dict


class Model(metaclass=ABCMeta):
    @abstractmethod
    def json(self):
        raise NotImplementedError

class MyModel(Model):
    pass