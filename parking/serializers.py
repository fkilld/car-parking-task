from rest_framework import serializers
from .models import *
class CarParkingDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarParkingDetails
        fields = '__all__'
        
        
