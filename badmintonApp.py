# -*- coding: utf-8 -*-
from flask import Flask, make_response
from flask_cors import CORS
import pymongo
import os
import settings 
from flask_restful import Resource, Api, reqparse
from crawler import googleExcelCrawler
import dbHandler
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": r"(.*).herokuapp.com|http://localhost.*"}})
class HelloWorld(Resource):
    def get(self):
        return "Hello from flask-rest"


class BadmintonInfoList(Resource):
    def get(self):
        return make_response(dumps(dbHandler.dbHandler.getbadmintonInfoList(),ensure_ascii=False))


class LocationInfoList(Resource):
    def get(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('location', type=str, help='location must be string')
        args = self.parser.parse_args()      
        return make_response(dumps(dbHandler.dbHandler.getLocationInfoList(args['location']),ensure_ascii=False))


class CrawlerBadmintonExcelList(Resource):
    def get(self):
        return googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1--VQHKN0mG-1CwxS_QKbpvFxtfQsDYrUS6PO-fDeIJo")
api.add_resource(HelloWorld, '/')
api.add_resource(LocationInfoList,'/api/locationinfolist')
api.add_resource(BadmintonInfoList,'/api/badmintoninfolist')

api.add_resource(CrawlerBadmintonExcelList,'/crawler')

if __name__ == "__main__":
    app.run()
