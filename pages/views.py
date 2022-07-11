from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
    
# def home(request):
#     return render(request, 'pages/home.html')

class About(TemplateView):
    template_name = 'pages/about.html'

class Services(TemplateView):
    template_name = 'pages/services.html'

class Contact(TemplateView):
    template_name = 'pages/contact.html'