from django.db import models

# Create your models here.
class FBV_MODEL(models.Model):
    enumber=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddrs=models.CharField(max_length=30)
