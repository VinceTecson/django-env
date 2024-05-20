from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display= ("prodName", "price", "image", "category_id")

admin.site.register(Products, ProductsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ("id", "category",)

admin.site.register(Category, CategoryAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display= ("product", "quantity", "user", "date_added",)

admin.site.register(Carts, CartAdmin)