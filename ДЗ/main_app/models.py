from django.db import models
from django.utils import timezone


class Participant(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    bdate = models.DateTimeField('birthdate')
    def getFIO(self):
        return "%s %s %s" % (self.lname, self.fname, self.patronymic)
    def __str__(self):
        return "%s %s" % (self.getFIO(), self.bdate) 
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateTimeField(default=timezone.now())
    where = models.CharField(max_length=500, default='Moscow')
    description = models.CharField(max_length=1000, default='')
    img = models.CharField(max_length=200, default='')
    def __str__(self):
        return "%s at %s" % (self.name, self.when)

    
    
class Participation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return "Participant = %d, Event = %d" % (self.participant, self.event) 
