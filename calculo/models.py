from django.db import models

# Create your models here.
class Segment(models.Model):
    _id = models.IntegerField()
    length = models.FloatField()
    height = models.FloatField()
    horizontaltube = models.IntegerField()
    gatecount = models.IntegerField()

    @property
    def verticaltubecount(self):
        length = ceil(self.length)
        while length % 3 != 0: 
            length = length +1
        return length/3

    @property
    def segmentnarea(self):
        segmentarea = self.length*self.height
        return segmentarea

    @property
    def segmentconnectiontopcount(self):
        connectiontop = (self.length/3)-1
        return connectiontop

    @property
    def segmentconnectionmidcount(self):
        if self.horizontaltube == 1:
            connectionmid = 0
        else: 
            connectionmid = ((self.length/3)-1)*(self.horizontaltube-1)
        return connectionmid
  
    @property
    def segmentwirecount(self):
        segmentwire = self.segmentarea*0.06 
        return segmentwire