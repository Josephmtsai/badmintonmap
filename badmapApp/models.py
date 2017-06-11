from django.db import models

# Create your models here.
class Location(models.Model):
	address = models.StringProperty()
	lat = models.FloatProperty()
	lng = models.FloatProperty()
	name = models.StringProperty()
class badmintonInfo(models.Model):
    startTime  = models.DateTimeProperty()
    endTime =models.DateTimeProperty()
    weekDay = models.StringProperty()
    weekDayInt =  models.IntegerProperty()
    contactPhone = models.StringProperty()
    contactName =  models.StringProperty()
    payInfo = models.IntegerProperty()
    location =  models.StringProperty()
    source = models.StringProperty()
    sourceData = models.StringProperty()
    lat = models.FloatProperty()
    lng = models.FloatProperty()
    address = models.StringProperty()
    created = models.DateTimeProperty(auto_now_add=True)
    line = models.StringProperty() 
    Key = models.StringProperty()	