from django.urls import path
from . import views

urlpatterns = [
    path('food_storage/', views.food_storage, name='food_storage'),
    path('add_foods/', views.add_foods, name='add_foods')
] 