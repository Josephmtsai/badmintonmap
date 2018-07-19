# TW-badminton-map

> badminton map in Taiwan

## Requirements

python 3.x install

## Build Setup

``` bash
# first create virtual env
python -m venv c:\path\to\myenv 

# clone the project use git or download and extract to the folder

# use the virtual env

Scripts\activate 
>if suceess will see the virtual env nam 

#then  install dependencies
pip install -r requirements.txt

#create .env file and excute the command to pull the envirment variable to local 

heroku config:get GoogleAuthKey -s  >> .env --app=qatbadmap
heroku config:get MONGODB_URI -s  >> .env --app=qatbadmap
heroku config:get LineBotApi -s  >> .env --app=qatbadmap
heroku config:get WebhookSECRET -s  >> .env --app=qatbadmap
```

## Start program

``` bash
python badmintonApp.py
```

## Debug mode

Auto reload when code change, see [flask-debug-mode](http://flask.pocoo.org/docs/0.12/quickstart/#debug-mode)

``` bash
set FLASK_DEBUG=1
set FLASK_APP=badmintonApp.py
flask run
```

## Reference

[Flask](http://flask.pocoo.org/docs/0.12/quickstart/#)