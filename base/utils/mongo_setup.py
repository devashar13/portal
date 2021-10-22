
import pymongo
from pymongo import MongoClient
cluster = MongoClient('localhost:27017')
db = cluster['Portal']
collection = db['kt_production.hotel']