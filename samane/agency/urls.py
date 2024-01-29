from django.urls import path
from agency import views

urlpatterns = [
    path("get_agencyuser_all", views.get_agencyuser_all),
    path("get_agency_all", views.get_agency_all),
    path("create_agencyuser", views.create_agencyuser),
]
