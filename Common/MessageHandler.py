import Common
# -*- coding: utf-8 -*-
def getBadmintonDataFromLocation(result,currentLocation,topNums=10):
    badmintonInfoArray = []
    for document in result:    
        badmintonInfo = {}
        badmintonInfo['location'] =  document['location']
        badmintonInfo['startTime']  =  document['startTime']
        badmintonInfo['endTime']  =  document['endTime']
        badmintonInfo['distance']  = Common.Common.getLocationDistance(currentLocation,document)
        badmintonInfo['contactName'] =  document['contactName'] 
        badmintonInfo['contactPhone'] =  document['contactPhone'] 
        badmintonInfo['payInfo'] =  document['payInfo'] 
        badmintonInfo['level']  =  document['payInfo']  
        badmintonInfoArray.append(badmintonInfo)
    return convertDataToString(sorted(badmintonInfoArray, key=lambda x: x['distance'])[:topNums])
def convertDataToString(sortedResult,maxCounter=999):
    message = ''
    counter =0
    for data in sortedResult:      
        if counter < maxCounter: 
            message +=  data['location'] +" \n"
            message +=  data['startTime'] + " ~ " +  data['endTime'] + " \n"
            message +=  data['contactName'] + " ~ " +  data['contactPhone'] + " \n"
            message +=  "價格: " + str(data['payInfo']) +  " \n"
            message +=  "程度:" +data['payInfo']  + "\n\n"  
    return message        