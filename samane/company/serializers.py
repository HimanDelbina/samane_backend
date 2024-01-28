from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = "__all__"
        depth = 1
        
class DriverGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = "__all__"
        
class MoneySerializers(serializers.ModelSerializer):
    class Meta:
        model = MoneyModel
        fields = "__all__"
        