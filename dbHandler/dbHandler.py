import pymongo
from bson.json_util import dumps
import os
MONGO_URL = os.environ.get('MONGODB_URI')


def getLocationInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    return dumps(db.locationInfo.find())


def insertLocationInfoList(locationInfoList):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    if len(locationInfoList) > 0:
        db.locationInfo.insert_many(locationInfoList)
        print("Insert OK")
        return "OK"
    return "Nothing Insert"

def getLocationInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    return dumps(db.LocationList.find())
def insertbadmintonInfoList(badmintonInfoList):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    if len(badmintonInfoList) > 0:
        db.badmintonInfo.insert_many(badmintonInfoList)
        print("Insert BadmintonList OK")
        return "OK"
    return "Nothing Insert"
def getbadmintonInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    return dumps(db.badmintonInfo.find({}))
def deleteAllbadmintonInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    db.badmintonInfo.delete_many({})
    return "Delete OK"