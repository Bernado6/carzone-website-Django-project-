from django.urls import path
from . import views

urlpatterns = [
  path('', views.Cars.as_view(), name = 'cars'),
]