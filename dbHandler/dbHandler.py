# -*- coding: utf-8 -*-
import pymongo
from bson.json_util import dumps
import os
import settings
from datetime import datetime, timedelta
from pytz import timezone
import pytz
tw = timezone('Asia/Taipei')
from Common import Common
MONGO_URL = os.environ.get('MONGODB_URI')


def insertStatus(status):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    db.status.insert_one(status)    

def insertLocationInfoList(locationInfoList):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    if len(locationInfoList) > 0:
        db.locationInfo.insert_many(locationInfoList)
        print("Insert OK")
        return "OK"
    return "Nothing Insert"

def getLocationInfoList(locationName=None):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    if locationName is not None:
        print(locationName)
        return db.locationInfo.find({'name':locationName})
    else:
        return db.locationInfo.find({})
def insertbadmintonInfoList(badmintonInfoList):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    if len(badmintonInfoList) > 0:
        deleteAllbadmintonInfoList()
        db.badmintonInfo.insert_many(badmintonInfoList)
        print("Insert BadmintonList OK")
        return "OK"
    return "Nothing Insert"
def getbadmintonInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    return db.badmintonInfo.find({},{'_id':0})
def getbadmintonInfoListByParameter(parameter):
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    if parameter == 'now':
        weekday = 0 if datetime.datetime.now().astimezone(tw).isoweekday() == 7 else datetime.datetime.now().astimezone(tw).isoweekday() +
        result = db.badmintonInfo.find({"$and": [{"startHour": {"$gt": 17}},{'weekDayInt':weekday}]})    
    else:
        weekday = 0 if datetime.datetime.now().astimezone(tw).isoweekday() +1 == 7 else datetime.datetime.now().astimezone(tw).isoweekday() +1
        result = db.badmintonInfo.find({"$and": [{"startHour": {"$gt": 17}},{'weekDayInt':weekday}]})    
    return result

def deleteAllbadmintonInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    db.badmintonInfo.delete_many({})
    return "Delete OK"
