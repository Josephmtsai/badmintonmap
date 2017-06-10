from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
import pymongo
import os
import datetime

MONGO_URL = os.environ.get('MONGODB_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/rest";
@sched.scheduled_job('interval', minutes=1)
def timed_job():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    db.testing.insert_one({"x": 10,"date":datetime.datetime.now()})
    print('This job is run every one minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()