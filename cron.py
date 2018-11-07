from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import os
import datetime
import requests
from crawler import googleExcelCrawler

sched = BlockingScheduler()
#test
@sched.scheduled_job('interval', minutes=720)
def crawler_job():
    googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1stkgvDFxKNf5V6Ozu7RMAK57oWzZkUNrfruXuiY1cDc")
    print('This job is insert data')
    print('This job is run every 720 minutes.')
@sched.scheduled_job('interval', minutes=60)
def timed_job():
    response = requests.get(os.environ.get('CURRENTDOMAIN'))
    print("Current Page Status " +str(response.status_code ))

sched.start()
