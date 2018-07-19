import Common
# -*- coding: utf-8 -*-
def getBadmintonDataFromLocation(result,currentLocation,topNums=10):
    badmintonInfoArray = []
    for document in result:    
        badmintonInfo = {}
        badmintonInfo['location'] =  document['location']
        badmintonInfo['startTime']  =  document['startTime']
        badmintonInfo['endTime']  =  document['endTime']
        badmintonInfo['distance']  = Common.getLocationDistance(currentLocation,document)
        badmintonInfo['contactName'] =  document['contactName'] 
        badmintonInfo['contactPhone'] =  document['contactPhone'] 
        badmintonInfo['payInfo'] =  document['payInfo'] 
        badmintonInfoArray.append(badmintonInfo)
    sortedResult = sorted(badmintonInfoArray, key=lambda x: x['distance'])[:topNums]
    message = ''
    for data in sortedResult:
        message
        message += "地點: " + data['location'] + " "
        message += "時間: " + data['startTime'] + " ~ " +  data['endTime'] + " \n"
        message += data['contactName'] + " ~ " +  data['contactPhone'] + " \n"
        message += "價格: " + str(data['payInfo']) +  " \n\n"
    return message