from django.urls import path
from tell import views

urlpatterns = [
    path("get_tell", views.get_tell),
]
