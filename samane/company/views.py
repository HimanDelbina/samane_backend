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



@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    s_data = request.data
    users = UserSerializers(data=s_data)
    data = {}
    user_check = UserModel.objects.filter(phone_number=request.data["phone_number"]).first()
    if user_check is not None:
        return Response("user is allow...", status=status.HTTP_208_ALREADY_REPORTED)
    else:
        if users.is_valid():
            account = users.save()
            data["first_name"] = account.first_name
            data["last_name"] = account.last_name
            data["phone_number"] = account.phone_number
            data["post"] = account.post
            data["is_driver"] = account.is_driver
            data["is_admin"] = account.is_admin
            data["is_tell"] = account.is_tell
            data["is_driver_role"] = account.is_driver_role
            data["is_cartex"] = account.is_cartex
            data["is_store_manager"] = account.is_store_manager
            data["password"] = account.password
            data["create_at"] = account.create_at
            data["update_at"] = account.update_at
            token = MyOwnToken.objects.get(userTokens=account).key
            data["token"] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response("user not create...", status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    info = {}
    user = UserModel.objects.filter(
        company_code=request.data["company_code"], password=request.data["password"]).first()

    if user is not None:
        token = MyOwnToken.objects.get(userTokens=user).key
        info["id"] = user.id
        info["first_name"] = user.first_name
        info["last_name"] = user.last_name
        info["phone_number"] = user.phone_number
        info["company_code"] = user.company_code
        info["post"] = user.post
        info["is_driver"] = user.is_driver
        info["is_admin"] = user.is_admin
        info["is_tell"] = user.is_tell
        info["is_driver_role"] = user.is_driver_role
        info["is_scan"] = user.is_scan
        info["is_pm"] = user.is_pm
        info["is_cartex"] = user.is_cartex
        info["password"] = user.password
        info["is_store_manager"] = user.is_store_manager
        info["create_at"] = user.create_at
        info["update_at"] = user.update_at
        info["token"] = token
        return Response(info, status=status.HTTP_200_OK)
    else:
        return Response('The entered data is incorrect', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def delete_user_by_id(request, id):
    user_data_for_delete = UserModel.objects.filter(id=id)
    user_data_for_delete.delete()
    return Response("user is delete...", status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def edit_user(request):
    etid_data = request.data
    edit_data_find_in_database = UserModel.objects.get(id=etid_data['id'])
    edit_data_find_in_database.first_name = etid_data['first_name']
    edit_data_find_in_database.last_name = etid_data['last_name']
    edit_data_find_in_database.phone_number = etid_data['phone_number']
    edit_data_find_in_database.post = etid_data['post']
    edit_data_find_in_database.is_driver = etid_data['is_driver']
    edit_data_find_in_database.is_admin = etid_data['is_admin']
    edit_data_find_in_database.is_tell = etid_data['is_tell']
    edit_data_find_in_database.is_driver_role = etid_data['is_driver_role']
    edit_data_find_in_database.is_cartex = etid_data['is_cartex']
    edit_data_find_in_database.is_store_manager = etid_data['is_store_manager']
    edit_data_find_in_database.password = etid_data['password']
    edit_data_find_in_database.save()
    return Response("user is update succesfully....", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_user(request):
    user_data = UserModel.objects.all()
    return Response(UserSerializers(user_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_driver_users(request):
    user_data = DriverModel.objects.all()
    return Response(DriverSerializers(user_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_driver_users(request,driver_id):
    data = DriverModel.objects.filter(id=driver_id)
    serializer_data = DriverSerializers(data=data, many=True)
    serializer_data.is_valid()
    serializer_data.save()
    return Response(serializer_data.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_driver_direction(request):
    get_data = request.data
    edit_data_find_in_database = DriverGetSerializers(data=get_data)
    money_data = MoneyModel.objects.all()
    money_user = 0
    money_driver = 0
    driver_length = get_data['len']
    for data in money_data:
        money_user = data.money_user
        money_driver = data.money_driver
    set_user_money = int(money_user) * int(driver_length)
    final = int(set_user_money) + int(money_driver)
    # print(set_user_money)
    # print(money_driver)
    # print(final)
    get_data['driver_money'] = str(money_driver)
    get_data['user_money'] = str(set_user_money)
    get_data['all_money'] = str(final)
    edit_data_find_in_database.driver = get_data['driver']
    edit_data_find_in_database.direction = get_data['direction']
    edit_data_find_in_database.len = get_data['len']
    edit_data_find_in_database.users = get_data['users']
    edit_data_find_in_database.driver_money = get_data['driver_money']
    edit_data_find_in_database.user_money = get_data['user_money']
    edit_data_find_in_database.all_money = get_data['all_money']
    edit_data_find_in_database.is_active = get_data['is_active']
    edit_data_find_in_database.is_accept = get_data['is_accept']
    if edit_data_find_in_database.is_valid():
        edit_data_find_in_database.save()
        return Response("direction is succesfully create", status=status.HTTP_200_OK)
    return Response("direction not create", status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_driver_data(request,driver_id):
    driver_data = DriverModel.objects.filter(driver=driver_id)
    return Response(DriverSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_driver_data_accept(request):
    driver_data = DriverModel.objects.filter(is_accept=True,is_active=True)
    return Response(DriverSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_driver_data_reject(request):
    driver_data = DriverModel.objects.filter(is_accept=False,is_active=True)
    return Response(DriverSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_driver_data_wait(request):
    driver_data = DriverModel.objects.filter(is_accept=False,is_active=False)
    return Response(DriverSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def change_password(request):
    old_password = request.data["old_password"]
    new_password = request.data["new_password"]
    user_id = request.data["user_id"]
    my_user_find = UserModel.objects.filter(id=user_id).first()
    if(my_user_find is not None):
        existpass = my_user_find.password
        if(existpass == old_password):
            my_user_find.password = new_password
            my_user_find.save()
            return Response("password changed", status=status.HTTP_200_OK)
        else:
            return Response("old password not true", status=status.HTTP_204_NO_CONTENT)
    else:
        return Response('user not found', status=status.HTTP_204_NO_CONTENT)
    
    
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_driver_data(request,driver_id):
#     driver_data = DriverModel.objects.filter(driver=driver_id)
    
#     return Response(DriverSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def get_driver_data(request):
#     driver_id = request.data['driver_id']
#     # driver_data = DriverModel.objects.get(driver=driver_id)
#     driver_data = DriverModel.objects.filter(driver=driver_id)
#     # driver_data = DriverModel.objects.filter(driver=driver_id).values_list(flat=True)
#     print("himan............................................................................")
#     print(driver_data)
#     print("himan............................................................................")
#     return Response(DriverGetSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_driver_data_all(request):
    driver_data = DriverModel.objects.all()
    return Response(DriverSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_driver(request):
    driver_data = UserModel.objects.filter(is_driver=True).values()
    return Response(UserSerializers(driver_data, many=True).data, status=status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([AllowAny])
def change_password(request):
    old_password = request.data["old_password"]
    new_password = request.data["new_password"]
    user_id = request.data["user_id"]
    my_user_find = UserModel.objects.filter(id=user_id).first()
    if(my_user_find is not None):
        existpass = my_user_find.password
        if(existpass == old_password):
            my_user_find.password = new_password
            my_user_find.save()
            return Response("password changed", status=status.HTTP_200_OK)
        else:
            return Response("old password not true", status=status.HTTP_204_NO_CONTENT)
    else:
        return Response('user not found', status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def edit_direction_data(request):
    etid_data = request.data
    edit_data_find_in_database = DriverModel.objects.get(id=etid_data['id'])
    edit_data_find_in_database.is_active = etid_data['is_active']
    edit_data_find_in_database.is_accept = etid_data['is_accept']
    edit_data_find_in_database.save()
    return Response("user is update succesfully....", status=status.HTTP_200_OK)

