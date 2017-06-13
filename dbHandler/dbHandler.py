import pymongo
from bson.json_util import dumps
MONGO_URL = os.environ.get('MONGODB_URI')


def getLocationInfoList():
    client = pymongo.MongoClient(MONGO_URL)
    db = client.heroku_szv1xx0f
    return dumps(db.LocationList.find())