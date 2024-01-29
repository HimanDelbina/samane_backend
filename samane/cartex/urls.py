from django.urls import path
from cartex import views

urlpatterns = [
    path("create_cartex", views.create_cartex),
    path("get_cartex_user/<int:id>", views.get_cartex_user),
    path("get_all_cartex", views.get_all_cartex),
    path("get_cartex_user_always/<int:id>", views.get_cartex_user_always),
    path("get_cartex_user_temporary/<int:id>", views.get_cartex_user_temporary),
    path("cartex_user_back", views.cartex_user_back),
    path("get_cartex_manager", views.get_cartex_manager),
    path("cartex_accept_manager", views.cartex_accept_manager),
]
