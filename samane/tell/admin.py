from django.contrib import admin

from .models import *

# Register your models here.


class TellAdmin(admin.ModelAdmin):
    fields = ["phone", "title"]
    list_display = ["phone", "title"]
    search_fields = ['phone', 'title']


admin.site.register(TellModel, TellAdmin)
