from django.db import models
from company.models import *




class CartexModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='نام کالا')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کارمند')
    is_temporary = models.BooleanField(default=False,verbose_name="موقت")
    is_always = models.BooleanField(default=False,verbose_name="دایم")
    is_back = models.BooleanField(default=False,verbose_name="برگشت کالا")
    is_manager = models.BooleanField(default= False , verbose_name="تایید ادمین")
    create_at = models.DateTimeField(auto_now_add=True)
    update_st = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "کارتکس انبار"
        verbose_name_plural = "کارتکس های انبار"

    def __str__(self):
        return self.title