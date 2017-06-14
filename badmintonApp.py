from flask import Flask
app = Flask(__name__)
import pymongo
from bson.json_util import dumps
from flask_restful import Resource, Api
from crawler import googleExcelCrawler
import dbHandler
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class getBadmintonInfoList(Resource):
    def get(self):
        return dbHandler.dbHandler.getbadmintonInfoList()


class CrawlerBadmintonExcelList(Resource):
    def get(self):
        return googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'),"1sdEYj_w57iQaFhD5eNNOMLEhMbzlnhs7vR8Lz5RlChA")
api.add_resource(HelloWorld, '/')
api.add_resource(getBadmintonInfoList,'/api/getBadmapInfoList')
api.add_resource(CrawlerBadmintonExcelList,'/crawler')

if __name__ == "__main__":
    app.run()