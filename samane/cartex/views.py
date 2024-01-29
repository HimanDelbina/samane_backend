from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['POST'])
@permission_classes([AllowAny])
def create_cartex(request):
    d_data = request.data
    cartex_data_serializer = CartexSerializers(data=d_data)
    if cartex_data_serializer.is_valid():
        cartex_data_serializer.save()
        return Response(cartex_data_serializer.data, status=status.HTTP_201_CREATED)
    return Response("message not send...", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cartex_user(request,id):
    driver_data = CartexModel.objects.filter(user_id=id)
    return Response(CartexSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cartex_user_always(request,id):
    cartex_data = CartexModel.objects.filter(user_id=id)
    data_pass =[]
    ser = CartexSerializers(cartex_data, many=True).data
    for data in ser:
        if data['is_always'] == True and data['is_manager'] == False:
            print(data)
            data_pass.append(data)
    return Response(data_pass, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_cartex_user_temporary(request,id):
    cartex_data = CartexModel.objects.filter(user_id=id)
    data_pass =[]
    ser = CartexSerializers(cartex_data, many=True).data
    for data in ser:
        if data['is_temporary'] == True and data['is_manager'] == False:
            data_pass.append(data)
    return Response(data_pass, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_cartex(request):
    data = CartexModel.objects.all()
    return Response(CartexSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cartex_manager(request):
    cartex_data = CartexModel.objects.all()
    data_pass =[]
    ser = CartexDataSerializers(cartex_data, many=True).data
    for data in ser:
        if data['is_back'] == True and data['is_manager'] == False:
            data_pass.append(data)
    return Response(data_pass, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def cartex_user_back(request):
    etid_data = request.data
    edit_data_find_in_database = CartexModel.objects.get(id=etid_data['id'])
    edit_data_find_in_database.is_back = etid_data['is_back']
    edit_data_find_in_database.save()
    return Response("cartex is back succesfully....", status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def cartex_accept_manager(request):
    etid_data = request.data
    edit_data_find_in_database = CartexModel.objects.get(id=etid_data['id'])
    edit_data_find_in_database.is_manager = etid_data['is_manager']
    edit_data_find_in_database.save()
    return Response("cartex is accept with manager succesfully....", status=status.HTTP_200_OK)