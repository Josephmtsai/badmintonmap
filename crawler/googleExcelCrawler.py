import os 
import django
from myapp import models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "badmap.settings")
django.setup()
import Common
def syncExcelToDB(apiKey,excelsheetid): 
	sheetList = [u'日',u'一',u'二',u'三',u'四',u'五',u'六']
	service = discovery.build('sheets', 'v4', developerKey=CONFIGPARSER.get("DEFAULT", "apikey"),discoveryServiceUrl='https://sheets.googleapis.com/$discovery/rest?version=v4')
	result = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,ranges=sheetList).execute()
	responseSheet = result.get('valueRanges', [])	
	weekDay = Common.getTodayWeekDay()
	#existlocationDict =googleMapLocation.getExistLocationToDict()
	newLocationDict = {}
	badmintonInfoList = []
	coordinate = None
	address = None
	for index,sheet in enumerate( responseSheet):
		rows =sheet.get('values',[])
		for rowIndex,row in  enumerate( rows):  
			if rowIndex == 1 or rowIndex ==0:
				continue
			badmintonInfo = models.badmintonInfo() 
			try:
				if len(row) > 8:
					badmintonInfo.location = row[1]
					"""
					if existlocationDict is not None and badmintonInfo.location.encode('UTF-8') not in existlocationDict:
						coordinate,address =  googleMapLocation.getLocationInfo(row[3]) 
					if coordinate is not None:
						badmintonInfo.address = address
						badmintonInfo.lat = coordinate['lat']
						badmintonInfo.lng = coordinate['lng']
						newLocationDict = googleMapLocation.locationToDict(newLocationDict,existlocationDict,badmintonInfo.location,address,coordinate)
					"""
					badmintonInfo.payInfo = Common.convertToInt(row[6])
					badmintonInfo.contactName = row[7]
					badmintonInfo.contactPhone = row[8]
					badmintonInfo.startTime = Common.convertToDateTime(row[0].split("~")[0],index -weekDay)	
					badmintonInfo.endTime = Common.convertToDateTime(row[0].split("~")[1],index -weekDay)
					badmintonInfo.weekDay = sheetList[index]
					badmintonInfo.weekDayInt = index
					badmintonInfo.source = "excel"
					badmintonInfo.line = row[9] if len(row) > 9 else ""
					badmintonInfo.sourceData = ",".join(row ) 
					#break
			finally:					
				badmintonInfoList.append(badmintonInfo)
	return badmintonInfoList
		#insertLocationInfoList(newLocationDict)