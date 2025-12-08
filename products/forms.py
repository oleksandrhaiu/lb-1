from django.forms import ModelForm, TextInput, NumberInput, Select
from .models import Product, Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва категорії'
            })
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'price', 'product_qty']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва товару'
            }),
            'category': Select(attrs={
                'class': 'form-control'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна'
            }),
            'product_qty': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кількість'
            }),
        }