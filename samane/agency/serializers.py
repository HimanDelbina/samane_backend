from rest_framework import serializers
from .models import *


class AgencySerializers(serializers.ModelSerializer):
    class Meta:
        model = AgencyModel
        fields = "__all__"
        
        
class AgencyUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = AgencyUserModel
        fields = "__all__"