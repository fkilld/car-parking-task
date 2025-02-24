from django.db import models

# Create your models here.

class CarParkingDetails(models.Model):
    car_number = models.CharField(max_length=100,unique=True,blank=False,null=False)
    car_name = models.CharField(max_length=100)
    inTime = models.DateTimeField(auto_now_add=True,blank=True)
    outTime = models.DateTimeField(null=True,blank=True)
    totalSpendTime = models.FloatField(null=True,blank=True)
    
    
    
    
