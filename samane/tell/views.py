from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status
import json


@api_view(["GET"])
@permission_classes([AllowAny])
def get_tell(request):
    data = TellModel.objects.all()
    return Response(TellSerializers(data, many=True).data, status=status.HTTP_200_OK)
