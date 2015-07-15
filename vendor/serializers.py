from rest_framework import serializers
from vendor.models import ResID


class ResIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResID
        fields = ('name', 'logo')

