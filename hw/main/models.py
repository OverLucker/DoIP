from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

default_image_path = 'images/default.jpg'

class Event(models.Model):
    name = models.CharField( max_length=50 )
    address = models.CharField( max_length = 100 )
    time = models.DateTimeField( default=timezone.now )
    desc = models.CharField( max_length=2000, null=True  )
    imageUrl = models.CharField( default=default_image_path, max_length=256, null=False )
    participation = models.ManyToManyField( User )
    
    def __str__(self):
        return "Name = %s, Country = %s, sportType = %s" % (self.name, self.time, self.address) 
        
        
# class Team(models.Model):
    # name = models.CharField( max_length=50 )
    # country = models.CharField( max_length = 30 )
    # sportType = models.CharField( max_length = 30 )
    # prizeCount = models.IntegerField()
    # desc = models.CharField( max_length=2000, null=True  )
    # imageUrl = models.CharField( max_length=100, null=True )
    # betUsers = models.ManyToManyField( User )
    
    # def __str__(self):
        # return "Name = %s, Country = %s, sportType = %s" % (self.name, self.country, self.sportType) 
