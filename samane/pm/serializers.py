from rest_framework import serializers
from .models import *


class DeviceEngineSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeviceEngineModel
        fields = "__all__"
        
class UnitSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnitModel
        fields = "__all__"
        
class PmObjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = PmObjectModel
        fields = "__all__"
