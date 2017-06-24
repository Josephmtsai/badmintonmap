from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import os
import datetime
import requests
from crawler import googleExcelCrawler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=360)
def crawler_job():
    googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA")
    print('This job is insert data')
    print('This job is run every 360 minutes.')
@sched.scheduled_job('interval', minutes=10)
def timed_job():
    response = requests.get(os.environ.get('CURRENTDOMAIN'))
    print("Current Page Status " +str(response.status_code ))

sched.start()