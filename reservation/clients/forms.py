import django.core.exceptions
from django import forms
from .models import ClientTypes, Client, Product, Order,ClientTypes

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientTypes
        fields = '__all__'

class ClientTypesForm(forms.ModelForm):
    class Meta:
        model = ClientTypes
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'