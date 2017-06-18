# -*- coding: utf-8 -*-
from flask import Flask, make_response
from flask_cors import CORS
import pymongo
import os
import settings 
from flask_restful import Resource, Api
from crawler import googleExcelCrawler
import dbHandler

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": r"(.*).herokuapp.com"}})
class HelloWorld(Resource):
    def get(self):
        return "你好 from flask-rest"


class BadmintonInfoList(Resource):
    def get(self):
        return make_response(dbHandler.dbHandler.getbadmintonInfoList())


class CrawlerBadmintonExcelList(Resource):
    def get(self):
        return googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA")
api.add_resource(HelloWorld, '/')
api.add_resource(BadmintonInfoList,'/api/badmintoninfolist')
api.add_resource(CrawlerBadmintonExcelList,'/crawler')

if __name__ == "__main__":
    app.run()