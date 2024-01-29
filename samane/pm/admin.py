from django.contrib import admin
from .models import *
# Register your models here.


class PmObjectAdmin(admin.ModelAdmin):
    fields = [
    "device","isbn",'barcode',
    "location","unit",'country_maker',
    "company_maker"
    ]
    list_display = ["device","location",'unit','image_tag']
    search_fields = ["device","isbn"]
    
class DeviceEngineAdmin(admin.ModelAdmin):
    fields = ["title"]
    list_display = ["title"]
    search_fields = ["title"]
    
class UnitAdmin(admin.ModelAdmin):
    fields = ["title"]
    list_display = ["title"]
    search_fields = ["title"]



admin.site.register(PmObjectModel, PmObjectAdmin)
admin.site.register(DeviceEngineModel, DeviceEngineAdmin)
admin.site.register(UnitModel, UnitAdmin)