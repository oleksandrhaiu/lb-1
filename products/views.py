from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category

class CategoryListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    ordering = ['title']

class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 5  # Кількість товарів на одній сторінці (для тесту)
    ordering = ['-created_at']