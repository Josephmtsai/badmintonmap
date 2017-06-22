# -*- coding: utf-8 -*- 
from urllib.request import urlopen
import urllib
import json 
from dbHandler import dbHandler
def getLocationInfo(address,apiKey):
    #print("https://maps.googleapis.com/maps/api/geocode/json?address="+ urllib.parse.quote(address)  + "&key="+apiKey)
    returnContent = urlopen("https://maps.googleapis.com/maps/api/geocode/json?address="+urllib.parse.quote(address)  + "&key="+apiKey).read().decode('utf-8')
    result = json.loads(returnContent)
    if result['status'] == "OK":
        if len( result['results']) > 0 :
            location = ''
            address = ''
            for possibleLocation in result['results']:
                location = possibleLocation['geometry']['location']
                address = possibleLocation['formatted_address']
                break
            return location,address,"OK"
        return None,None,"OK"
    return None,None,None
def getExistLocationToDict():
    locationList = dbHandler.getLocationInfoList()
    existLocationDict = {}
    if locationList is not None:
        for locationInfo in locationList:
            locationToDict(existLocationDict,{},locationInfo['name'],locationInfo['address'],{'lat':locationInfo['lat'],'lng':locationInfo['lng'],'name': locationInfo['name']})
    return existLocationDict

def locationToDict(newLocationDict,existLocationDict,location,address,coordinate):
    if location is not None and location.encode('UTF-8') not in existLocationDict:
        newLocationDict[location.encode('UTF-8')] = {'address':address ,'lat':coordinate['lat'],'lng':coordinate['lng'],'name': location }
    return newLocationDict

def dictToLocationInfoList(locationDict):
    locationList = []
    print(locationDict)
    if locationDict is not None:	
        for key in locationDict:
            locationList.append(locationDict[key])
    return locationList