from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet
from . import views

router = DefaultRouter()
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('food_storage/', views.food_storage, name='food_storage'),
    path('add_foods/', views.add_foods, name='add_foods')
] 