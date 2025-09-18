from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_moderator_main_page, name="moderator/index.html"),
    path('animals/create', views.animal_create, name="animals_create"),
    path('animals_m', views.show_animals, name="animals_m"),
    path('animals/<int:pk>', views.AnimalDetailView.as_view(), name="detail_view")
]