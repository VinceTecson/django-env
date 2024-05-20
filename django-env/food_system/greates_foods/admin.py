from django.contrib import admin
from .models import foods

class list_foods(admin.ModelAdmin):
    list_display = ('name', 'food_type', 'price')

admin.site.register(foods, list_foods)
