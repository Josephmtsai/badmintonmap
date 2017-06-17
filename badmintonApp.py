# -*- coding: utf-8 -*-
from flask import Flask, make_response
import pymongo
import os
import settings 
from flask_restful import Resource, Api
from crawler import googleExcelCrawler
import dbHandler

app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return "你好"


class getBadmintonInfoList(Resource):
    def get(self):
        return make_response(dbHandler.dbHandler.getbadmintonInfoList())


class CrawlerBadmintonExcelList(Resource):
    def get(self):
        return googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA")
api.add_resource(HelloWorld, '/')
api.add_resource(getBadmintonInfoList,'/api/getBadmapInfoList')
api.add_resource(CrawlerBadmintonExcelList,'/crawler')

if __name__ == "__main__":
    app.run()