from django.contrib import admin
from .models import *
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin


class AgencyUserResource(resources.ModelResource):
    published = Field(attribute='published', column_name='published_date')
    class Meta:
        model = AgencyUserModel
        fields = ('id', 'agency', 'users', 'direction','create_at')
        export_order = ('id', 'agency', 'users', 'direction','create_at')
        store_instance = True
        widgets = {
            'published': {'format': '%d.%m.%Y'},
        }

class AgencyAdmin(admin.ModelAdmin):
    fields = ["title"]
    list_display = ["title"]
    search_fields = ['title']
    
class AgencyUserAdmin(ImportExportModelAdmin):
    resource_classes = [AgencyUserResource]
    fields = [
        "agency",
        "users",
        "direction",
    ]
    list_display = ["agency","get_users","direction",'create_at']
    search_fields = ['agency']
    list_filter = ["create_at"]
    def get_users(self, instance):
        return [user.first_name for user in instance.users.all()]   
    
    
    

    
admin.site.register(AgencyModel, AgencyAdmin)
admin.site.register(AgencyUserModel, AgencyUserAdmin)