from rest_framework import serializers
from vendor.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Mata:
        model = Location
        fields = ('address', 'latitude', 'longitude')


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = ('open_time', 'close_time', 'm', 't', 'w', 'r', 'f', 's', 'h', 'leftTime')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price', 'calories', 'resid')
        

class ResIDSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)
    
    class Meta:
        model = ResID
        fields = ('name', 'logo', 'menu', 'dishes')


class UserMapSerializer(serializers.ModelSerializer):
    loc = LocationSerializer(read_only=True)
    hours = HoursSerializer(read_only=True)
    resid = ResIDSerializer(read_only=True)
    
    class Meta:
        model = UserMap
        fields = ('username', 'resid', 'hours', 'loc')








