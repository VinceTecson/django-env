from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from .models import foods
from django.urls import reverse
from django.template import loader
from .serializers import FoodSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = foods.objects.all()
    serializer_class = FoodSerializer

def food_storage(request):
    my_foods = foods.objects.all()
    return render(request, 'HM_food.html', {'my_foods': my_foods})

def add_foods(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        food_type = request.POST.get('food_type')
        price = request.POST.get('price')

        food_stored= foods.objects.create(name=name, food_type=food_type, price=price)

        return HttpResponseRedirect(reverse('food_storage'))
    else:
        return render(request, 'ADD_food.html')