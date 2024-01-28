from rest_framework import serializers
from .models import *


class TellSerializers(serializers.ModelSerializer):
    class Meta:
        model = TellModel
        fields = "__all__"
