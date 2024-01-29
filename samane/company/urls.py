from django.urls import path
from company import views

urlpatterns = [
    path("create_user", views.create_user),
    path("login_user", views.login_user),
    path("delete_user_by_id", views.delete_user_by_id),
    path("edit_user", views.edit_user),
    path("get_all_user", views.get_all_user),
    path("change_password", views.change_password),
    ##################################################
    path("get_all_driver", views.get_all_driver),
    path("get_all_driver_users", views.get_all_driver_users),
    path("get_driver_users/<int:driver_id>", views.get_driver_users),
    path("get_driver_data/<int:driver_id>", views.get_driver_data),
    path("get_driver_data_accept", views.get_driver_data_accept),
    path("get_driver_data_reject", views.get_driver_data_reject),
    path("get_driver_data_wait", views.get_driver_data_wait),
    path("get_driver_data_all", views.get_driver_data_all),
    path("add_driver_direction", views.add_driver_direction),
    path("edit_direction_data", views.edit_direction_data),
    ##################################################
]
