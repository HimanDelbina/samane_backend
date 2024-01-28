from django.contrib import admin
from .models import *
# Register your models here.


class PmObjectAdmin(admin.ModelAdmin):
    fields = [
    "title","isbn",'barcode'
    ]
    list_display = ["title","isbn",'image_tag']
    search_fields = ["title","isbn"]
    
    def get_users(self, instance):
        return [user.first_name for user in instance.users.all()]
    
admin.site.register(PmObjectModel, PmObjectAdmin)