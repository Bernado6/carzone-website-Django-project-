from ast import keyword
from django.views.generic import DetailView, TemplateView,ListView
from django.shortcuts import  render ,get_object_or_404
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Car
# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    color_fields = Car.objects.values_list('color',flat=True).distinct()
    location_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style',flat=True).distinct()

    data = {
        'cars':paged_cars,
        'color_fields':color_fields,
        'location_fields':location_fields,
        'year_fields':year_fields,
        'body_style_fields':body_style_fields,
    }
    return render(request, "cars/cars.html", data)

# class Cars(ListView):
#     model = Car
#     template_name = "cars/cars.html"
#     cars = Car.objects.order_by('-created_date')
#     page =None
#     paginator = Paginator(cars, 4)
    
#     def dispatch(self, request, *args, **kwargs):
#         self.request = request
#         self.page = request.GET.get('page')
#         return super().dispatch(request, *args, **kwargs)
    
#     paged_cars = paginator.get_page(page)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cars'] = self.paged_cars
#         return context

class CarDetail(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'single_car'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['single_car'] = get_object_or_404(Car, pk = pk)
        return context


class Search(TemplateView):
    template_name = 'cars/search.html'
    cars = Car.objects.order_by('-created_date')

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.page = request.GET.get('page')

        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                self.cars = self.cars.filter(description__icontains = keyword)
        
        if 'color' in request.GET:
            color = request.GET['color']
            if color:
                self.cars = self.cars.filter(color__iexact = color)

        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                self.cars = self.cars.filter(city__iexact = city)

        if 'year' in request.GET:
            year = request.GET['year']
            if year:
                self.cars = self.cars.filter(year__iexact = year)

        if 'body_style' in request.GET:
            body_style = request.GET['body_style']
            if body_style:
                self.cars = self.cars.filter(body_style__iexact = body_style)

        if 'min_price' in request.GET:
            min_price = request.GET['min_price']
            max_price = request.GET['max_price']
            if max_price:
                self.cars = self.cars.filter(price__gte = min_price, price__lte = max_price)

        return super().dispatch(request, *args, **kwargs)

        


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = self.cars
        return context
    
