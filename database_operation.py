import pymongo
import urllib
from pymongo import MongoClient
from market_data import get_stock_data
from iv import pull_iv

def connect_with_database():
    mongodb_uri= "mongodb+srv://saurav:"+ urllib.parse.quote("Saurav770@")+"@cluster0.z5nma.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client= MongoClient(mongodb_uri)
    global db
    db = client["market_data"]
    global collection
    collection = db["iv"]  

def insert_data_into_database(data):
    collection.insert_many(data)

def remove_data():
    collection.remove()





if __name__ == "__main__":
    #pull_iv('NIFTY')
    connect_with_database()
    #d1=get_stock_data('NIFTY')
    data,ce,pe=pull_iv('NIFTY')
    insert_data_into_database(ce)
    