from model.item import Item
from model.alert import Alert

url = "https://www.johnlewis.com/apple-iphone-11-ios-6-1-inch-4g-lte-sim-free-128gb/p4529033"
tag_name = "p"
query = {"class": "price price--large"}

iphone = Item(url, tag_name, query)
iphone.save_to_mongo()

#
items_load = Item.all()

alert = Alert("",800)
alert.save_to_mongo()