from rest_framework import serializers
from vendor.models import *

class ResIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResID
        fields = ('name', 'logo', 'menu')


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        models = Hours
        fields = ('open_time', 'close_time', 'm', 't', 'w', 'r', 'f', 's', 'h')

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        models = Menus
        fields = ('name', 'firstdish')

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        models = Dish
        fields = ('name', 'price', 'calories', 'nextdish')
