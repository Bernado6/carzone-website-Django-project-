from django.views.generic import DetailView, TemplateView
from .models import Car
# Create your views here.

class Cars(TemplateView):
    template_name = "cars/cars.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cars'] = Car.objects.all()
        return context