from rest_framework import serializers
from vendor.models import ResID
from vendor.models import Hours

class ResIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResID
        fields = ('name', 'logo', 'menu')


class HoursSerializer(serializers.ModelSerializer):
    class Mets:
        models = Hours
        fields = ('open_time', 'close_time', 'm', 't', 'w', 'r', 'f', 's', 'h')
