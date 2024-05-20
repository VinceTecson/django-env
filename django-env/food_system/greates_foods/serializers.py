from rest_framework import serializers
from .models import *

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = foods
        fields = ['name', 'food_type', 'price']

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = town
        fields = ['id', 'town']