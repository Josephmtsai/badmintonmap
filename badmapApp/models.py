from django.db import models

# Create your models here.
class Location(models.Model):
	address = models.TextField()
	lat = models.FloatField()
	lng = models.FloatField()
	name = models.TextField()
class badmintonInfo(models.Model):
    startTime  = models.TimeField()
    endTime =models.TimeField()
    weekDay = models.TextField()
    weekDayInt =  models.SmallIntegerField()
    contactPhone = models.TextField()
    contactName =  models.TextField()
    payInfo = models.SmallIntegerField()
    location =  models.TextField()
    source = models.TextField()
    sourceData = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.TextField()
    created = models.DateTimeProperty(auto_now_add=True)
    line = models.TextField() 
    Key = models.TextField()	