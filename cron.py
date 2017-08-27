from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import os
import datetime
import requests
from crawler import googleExcelCrawler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=360)
def crawler_job():
    googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1d2a4Zdl4PuXCsUPbqW-r3vGtwxJKoZs0oxQy4YsK4Wg")
    print('This job is insert data')
    print('This job is run every 360 minutes.')
@sched.scheduled_job('interval', minutes=3)
def timed_job():
    response = requests.get(os.environ.get('CURRENTDOMAIN'))
    print("Current Page Status " +str(response.status_code ))

sched.start()