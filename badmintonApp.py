# -*- coding: utf-8 -*-
from flask import Flask, make_response, request
from flask_cors import CORS
import pymongo
import os
import settings
from flask_restful import Resource, Api, reqparse
from crawler import googleExcelCrawler
import dbHandler
from bson.json_util import dumps
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, LocationMessage
from Common import MessageHandler
line_bot_api = LineBotApi(os.environ.get('LineBotApi'))
handler = WebhookHandler(os.environ.get('WebhookSECRET'))
app = Flask(__name__)
api = Api(app)
# cors = CORS(app, resources={r"/api/*": {"origins": r"(.*).herokuapp.com|http://localhost.*|(.*).mvrater.com"}})

cors = CORS(app, resources={r"/api/*": {"origins": r"*"}})


class HelloWorld(Resource):
    def get(self):
        return "Hello from flask-rest"


class BadmintonInfoList(Resource):
    def get(self):
        return make_response(dumps(dbHandler.dbHandler.getbadmintonInfoList(), ensure_ascii=False))


class LocationInfoList(Resource):
    def get(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('location', type=str,
                                 help='location must be string')
        args = self.parser.parse_args()
        return make_response(dumps(dbHandler.dbHandler.getLocationInfoList(args['location']), ensure_ascii=False))


class GetSheetNames(Resource):
    def get(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'sheetid', type=str, help='sheetid must be string')
        args = self.parser.parse_args()
        return make_response(dumps(googleExcelCrawler.getSheetNames(os.environ.get('GoogleAuthKey'), args['sheetid']), ensure_ascii=False))


class CrawlerBadmintonExcelList(Resource):
    def get(self):
        return googleExcelCrawler.syncExcelToDB(os.environ.get('GoogleAuthKey'), "1stkgvDFxKNf5V6Ozu7RMAK57oWzZkUNrfruXuiY1cDc")


class LineBotHandler(Resource):
    def post(self):
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']
        # get request body as text
        body = request.get_data(as_text=True)
        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'OK'

    def get(self):
        return make_response(dumps(dbHandler.dbHandler.getbadmintonInfoListByParameter('now'), ensure_ascii=False))


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "今天打球a":
        content = dbHandler.dbHandler.getbadmintonInfoListByParameter('now')
        if content.count() == 0:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(
                text="No badminton info right now"))
        else:
            locationMessage = MessageHandler.convertDataToString(content, 10)
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=locationMessage))

    elif event.message.text == "明天打球":
        content = dbHandler.dbHandler.getbadmintonInfoListByParameter(
            'tomorrow')
        if content.count() == 0:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(
                text="No badminton info right now"))
        else:
            locationMessage = MessageHandler.convertDataToString(content, 10)
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=locationMessage))
    else:
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(
            text=profile.display_name + '\n' + event.message.text + '\n UserId:' + event.source.user_id))


@handler.add(MessageEvent, message=LocationMessage)
def handle_Location_message(event):
    content = dbHandler.dbHandler.getbadmintonInfoListByParameter('now')
    locationTuple = (event.message.latitude, event.message.longitude)
    message = "今晚打球場地以距離判斷:\n"
    message += MessageHandler.getBadmintonDataFromLocation(
        content, locationTuple)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=message))


api.add_resource(HelloWorld, '/')
api.add_resource(LineBotHandler, '/callback')
api.add_resource(LocationInfoList, '/api/locationinfolist')
api.add_resource(BadmintonInfoList, '/api/badmintoninfolist')
api.add_resource(GetSheetNames, '/api/getsheetnames')

api.add_resource(CrawlerBadmintonExcelList, '/crawler')

if __name__ == "__main__":
    app.run()
