from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import binascii
import os
from django.utils import timezone


class UserModel(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="نام")
    last_name = models.CharField(max_length=30, verbose_name=" نام خانوادگی")
    phone_number = models.CharField(
        max_length=11, verbose_name="شماره موبایل", unique=True, blank=False, null=False
    )
    company_code = models.CharField(max_length=10 , verbose_name="کد پرسنلی",blank=False, null=False )
    post = models.CharField(max_length=20, blank=True, null=True, verbose_name="سمت")
    is_driver = models.BooleanField(default=False, verbose_name="آیا راننده است ؟")
    is_admin = models.BooleanField(
        default=False, verbose_name="آیا دسترسی ادمین دارد ؟"
    )
    is_tell =  models.BooleanField(
        default=True, verbose_name="آیا به بخش شماره تلفن ها دسترسی دارد ؟"
    )
    is_driver_role =  models.BooleanField(
        default=False, verbose_name="آیا به بخش راننده ها دسترسی دارد ؟"
    )
    is_scan = models.BooleanField(default=False, verbose_name="آیا به بخش بارکد خوان دسترسی دارد ؟")
    is_pm = models.BooleanField(default=False, verbose_name="آیا به بخش پی ام دسترسی دارد ؟")
    is_cartex=models.BooleanField(default=True, verbose_name="آیا به بخش کارتکس انبار دسترسی دارد ؟")
    is_store_manager = models.BooleanField(default = False ,verbose_name="آیا به بخش مدیریت انبار دسترسی دارد ؟" )
    password = models.CharField(max_length=20, verbose_name="رمز")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمندان"

    def __str__(self):
        return self.first_name


class DriverModel(models.Model):
    DIRECTION_CHOICES = (
        ('R', 'آمدن به شرکت'),
        ('W', 'برگشت از شرکت'),
    )
    driver = models.ForeignKey(
        UserModel, verbose_name="راننده", on_delete=models.CASCADE,related_name = "driver"
    )
    users = models.ManyToManyField(UserModel, verbose_name="کارمند",related_name = "user")
    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES, verbose_name="مسیر")
    driver_money = models.CharField(max_length=7)
    user_money = models.CharField(max_length=7)
    all_money = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False, verbose_name="تاییدیه")
    is_accept= models.BooleanField(default=False, verbose_name="تاییدیه نهایی")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "راننده "
        verbose_name_plural = " راننده ها"

    def __str__(self):
        return self.driver.first_name

class MoneyModel(models.Model):
    money_driver = models.CharField(max_length=7, verbose_name="مبلغ راننده")
    money_user = models.CharField(max_length=7, verbose_name="مبلغ مسافر")
    
    class Meta:
        verbose_name = "مبلغ "
        verbose_name_plural = " مبلغ ها"

    def __str__(self):
        return str(self.money_driver )
    
@receiver(post_save, sender=UserModel)
def create_auth_token(sender, instance=UserModel, created=False, **kwargs):
    if created:
        MyOwnToken.objects.create(userTokens=instance)


class MyOwnToken(models.Model):
    key = models.CharField(("Key"), max_length=40, primary_key=True)

    userTokens = models.OneToOneField(
        UserModel,
        related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name="user_token",
    )
    created = models.DateTimeField(("Created"), auto_now_add=True)

    class Meta:
        verbose_name = "userToken"
        verbose_name_plural = "userTokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(MyOwnToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Users Token"
        verbose_name_plural = "User Token"
