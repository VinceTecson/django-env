from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.category}"

class Products(models.Model):
    prodName = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category= models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f"{self.prodName} {self.price} {self.image}"

class Carts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} {self.product.prodName}'
    
