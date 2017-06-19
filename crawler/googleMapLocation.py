# -*- coding: utf-8 -*- 
from urllib.request import urlopen
import json 
from dbHandler import dbHandler
def getLocationInfo(address,apiKey):
    print(address.encode("UTF-8"))
    returnContent = urlopen("https://maps.googleapis.com/maps/api/geocode/json?address="+address.encode("UTF-8") + "&key="+apiKey).read().decode('utf8')
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
    locationList = dbHandler.getDBLocation()
    existLocationDict = {}
    if locationList is not None:
        for location in locationList:
            locationToDict(existLocationDict,{},location.name,location.address,{'lat':location.lat,'lng':location.lng})
    return existLocationDict

def locationToDict(newLocationDict,existLocationDict,location,address,coordinate):
    if location is not None and location.encode('UTF-8') not in existLocationDict:
        newLocationDict[location.encode('UTF-8')] = {'address':address ,'lat':coordinate['lat'],'lng':coordinate['lng'] }
    return newLocationDict

