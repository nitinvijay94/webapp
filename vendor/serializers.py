from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ResIDSerializer(serializers.ModelSerializer):
    class Meta:
            model = ResID
                    fields = ('name', 'logo')
