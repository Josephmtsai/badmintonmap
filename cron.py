from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()
import pymongo
import os
import datetime
import requests
from crawler import googleExcelCrawler

MONGO_URL = os.environ.get('MONGODB_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/rest";
@sched.scheduled_job('interval', minutes=360)
def crawler_job():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    badmintonInfoList = googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA")
    if len(badmintonInfoList) > 0:
        db.badmintonInfo.insert_many(badmintonInfoList)
        print('This job is insert data')
    print('This job is run every 360 minutes.')
@sched.scheduled_job('interval', minutes=3)
def timed_job():
    response = requests.get(os.environ.get('CURRENTDOMAIN'))
    print("Current Page Status " +str(response.status_code ))
sched.start()