from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.show_contacts),
    path('prices', views.show_prices),
    path('about', views.show_about)
]