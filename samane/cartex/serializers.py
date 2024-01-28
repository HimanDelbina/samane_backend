from rest_framework import serializers
from .models import *


class CartexSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartexModel
        fields = "__all__"
        
class CartexDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartexModel
        fields = "__all__"
        depth=1
