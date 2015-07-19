from rest_framework import serializers
from vendor.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'latitude', 'longitude')


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = ('open_time_m', 'close_time_m',
                'open_time_t', 'close_time_t', 
                'open_time_w', 'close_time_w', 
                'open_time_r', 'close_time_r', 
                'open_time_f', 'close_time_f', 
                'open_time_s', 'close_time_s', 
                'open_time_h', 'close_time_h', 
                'm', 't', 'w', 'r', 'f', 's', 'h', 'leftTime')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price', 'calories', 'resid')


class UserMapSerializer(serializers.ModelSerializer):
    loc = LocationSerializer(read_only=True)
    hours = HoursSerializer(read_only=True)
    
    class Meta:
        model = UserMap
        fields = ('username', 'resid', 'hours', 'loc')


class ResIDSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)
    usermap = UserMapSerializer(read_only=True)

    class Meta:
        model = ResID
        fields = ('name', 'logo', 'menu', 'dishes', 'usermap')





