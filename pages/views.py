from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from . models import Team
from cars.models import Car
# Create your views here.
# def home(request):
#     teams = Team.objects.all()
#     data = {
#         'teams':teams,
#     }
#     return render(request, 'pages/home.html',data)


class Home(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['featured_cars'] = Car.objects.all().order_by('-created_date').filter(is_featured = True)
        context['all_cars'] = Car.objects.all().order_by('-created_date')
        # context['search_fields'] = Car.objects.values('model','state','city','year','body_style', 'transmission', 'color')
        context['color_fields'] = Car.objects.values_list('color',flat=True).distinct()
        context['location_fields'] = Car.objects.values_list('city',flat=True).distinct()
        context['year_fields'] = Car.objects.values_list('year',flat=True).distinct()
        context['body_style_fields'] = Car.objects.values_list('body_style',flat=True).distinct()
        return context


class About(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all().order_by('-id')

        return context

class Services(TemplateView):
    template_name = 'pages/services.html'

class Contact(TemplateView):
    template_name = 'pages/contact.html'