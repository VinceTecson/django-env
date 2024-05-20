from django import forms
from .models import *

class AdminAddProduct(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'