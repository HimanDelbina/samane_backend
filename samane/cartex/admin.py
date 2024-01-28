from django.contrib import admin
from .models import *
# Register your models here.


class CartexAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "user",
        'is_temporary',
        'is_always',
        'is_back',
        'is_manager',
    ]
    list_display = ["title","user",'is_temporary',
        'is_always',  'is_back',
        'is_manager',]
    list_filter = ["title","user",'is_temporary',
        'is_always']
    search_fields = ["title","user",'is_temporary',
        'is_always']
    
    def get_users(self, instance):
        return [user.first_name for user in instance.users.all()]
    
admin.site.register(CartexModel, CartexAdmin)


