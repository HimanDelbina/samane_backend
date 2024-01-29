from ast import Store
from asyncio.windows_events import NULL
from urllib import response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import *
from . serializers import *
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.decorators import permission_classes, api_view
from django.core.files.base import ContentFile
import base64
from rest_framework.response import Response



@api_view(['GET'])
@permission_classes([AllowAny])
def get_agencyuser_all(request):
    driver_data = AgencyUserModel.objects.all()
    return Response(AgencyUserSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_agency_all(request):
    driver_data = AgencyModel.objects.all()
    return Response(AgencySerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_agencyuser(request):
    d_data = request.data
    agency_data_serializer = AgencyUserSerializers(data=d_data)
    if agency_data_serializer.is_valid():
        agency_data_serializer.save()
        return Response(agency_data_serializer.data, status=status.HTTP_201_CREATED)
    return Response("message not send...", status=status.HTTP_400_BAD_REQUEST)