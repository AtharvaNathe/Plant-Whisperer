from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_form, name='plant_form'),
    path('result/', views.plant_result, name='plant_result'),
]
