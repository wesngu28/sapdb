from django.urls import path
from . import views

urlpatterns = [
  path('foods/', views.getFoods),
  path('packs/', views.getPacks)
]