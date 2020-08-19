from typing import Dict
import re
import requests
from bs4 import BeautifulSoup


class Item:
    def __init__(self, url: str, tag_name: str, query: Dict):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        # regular expresion
        pattern = re.compile(r"(\d+,?\d*\.\d\d?)")  # 15.95
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
        return self.price
