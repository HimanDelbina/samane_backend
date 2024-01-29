from django.db import models
from company.models import *
# Create your models here.

class AgencyModel(models.Model):
    title = models.CharField(max_length=50,verbose_name="نام آژانس")

    class Meta:
        verbose_name = "آژانس "
        verbose_name_plural = " آژانس ها"
        
    def __str__(self):
        return self.title    
    

class AgencyUserModel(models.Model):
    DIRECTION_CHOICES = (
        ('R', 'آمدن به شرکت'),
        ('W', 'برگشت از شرکت'),
    )
    agency = models.ForeignKey(AgencyModel, verbose_name="آژانس",related_name = "agency", on_delete=models.CASCADE)
    users = models.ManyToManyField(UserModel, verbose_name="کاربران")
    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES, verbose_name="مسیر")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ثبت آزانس "
        verbose_name_plural = " ثبت آژانس ها"

    def __str__(self):
        return self.direction