from flask import Flask
app = Flask(__name__)
import pymongo
from bson.json_util import dumps
from flask_restful import Resource, Api
from crawler import googleExcelCrawler
import os
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class getBadmintonInfoList(Resource):
    def get(self):
        client = pymongo.MongoClient(MONGO_URL)
        db = client.heroku_szv1xx0f
        return dumps(db.badmintonInfo.find())


class CrawlerBadmintonExcelList(Resource):
    def get(self):
        return googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA")
api.add_resource(HelloWorld, '/')
api.add_resource(getBadmintonInfoList,'/getBadmapInfoList')
api.add_resource(CrawlerBadmintonExcelList,'/crawler')

if __name__ == "__main__":
    app.run()