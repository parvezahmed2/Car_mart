from django.shortcuts import render

from cars.models import Car
from brand.models import CarModel
from django.shortcuts import render, get_object_or_404
# Create your views here.


# def home(request, brand_slug = None):
#     data = Car.objects.all()
#     if brand_slug is not None:
#         brand = CarModel.objects.get(slug = brand_slug)
#         data = Car.objects.filter(brand = brand)
#     brands = CarModel.objects.all()
#     return render(request, 'home.html', {'data' : data, 'brands' : brands})

def home(request, brand_slug=None):
    data = Car.objects.all()
    brands = CarModel.objects.all()

    if brand_slug:
        brand = get_object_or_404(CarModel, slug=brand_slug)
        data = Car.objects.filter(brand=brand)

    return render(request, 'home.html', {'data': data, 'brands': brands})


