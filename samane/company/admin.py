from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "company_code",
        "post",
        "password",
        "is_driver",
        "is_admin",
        "is_tell",
        "is_driver_role",
        "is_scan",
        "is_pm",
        "is_cartex",
        "is_store_manager",
        "is_agency",
    ]
    list_display = ["phone_number","company_code", "first_name", "last_name","post","is_driver",'is_admin']
    list_filter = ["is_driver", "is_admin","is_tell","is_driver_role",'is_store_manager','is_agency']
    search_fields = ['first_name', 'last_name', 'phone_number',"company_code"]


class DriverAdmin(admin.ModelAdmin):
    fields = [
        "driver",
        "users",
        "direction",
        "driver_money",
        "user_money",
        "all_money",
        "is_active",
        "is_accept",
    ]
    list_display = ["driver","get_users",'direction',
        "driver_money",
        "user_money",
        "all_money","is_active","is_accept"]
    
    
    def get_users(self, instance):
        return [user.first_name for user in instance.users.all()]
    
    
class MoneyAdmin(admin.ModelAdmin):
    fields = [
        "money_driver",
        "money_user"
    ]
    list_display = ["money_driver","money_user"]


admin.site.register(UserModel, UserAdmin)
admin.site.register(DriverModel, DriverAdmin)
admin.site.register(MoneyModel, MoneyAdmin)
# admin.site.register(DirectionModel, DirectionAdmin)
