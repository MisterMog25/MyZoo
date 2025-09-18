from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('contacts', views.show_contacts, name='contacts'),
    path('prices', views.show_prices, name='prices'),
    path('about', views.show_about, name='about'),
    path('animals_u', views.show_animals, name='animals_u')
]