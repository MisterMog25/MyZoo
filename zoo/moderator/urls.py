from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_admin_main_page, name="moderator/index.html"),
    path('create', views.animal_create, name="create")
]