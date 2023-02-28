from django.urls import path
from . import views

urlpatterns = [
  path('', views.cars, name = 'cars'),
  path('<int:pk>',views.CarDetail.as_view(), name = 'car_detail'),
  path('search', views.Search.as_view(), name= 'search')
]