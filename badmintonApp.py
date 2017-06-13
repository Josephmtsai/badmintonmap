from flask import Flask
app = Flask(__name__)
import pymongo
from bson.json_util import dumps

api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class getBadmintonInfoList(Resource):
    def get(self):
        client = pymongo.MongoClient(MONGO_URL)
        db = client.heroku_szv1xx0f
        return dumps(db.badmintonInfo.find())
api.add_resource(HelloWorld, '/')
api.add_resource(getBadmintonInfoList,'/getBadmapInfoList')

if __name__ == "__main__":
    app.run()