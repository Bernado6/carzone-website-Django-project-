from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('about', views.About.as_view(), name = 'about'),
    path('services', views.Services.as_view(), name = 'services'),
    path('contact', views.Contact.as_view(), name = 'contact'),
]