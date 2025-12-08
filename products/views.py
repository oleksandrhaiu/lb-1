from django.shortcuts import render
from django.views.generic import ListView, CreateView  # Додали CreateView
from django.urls import reverse_lazy  # Для перенаправлення після успіху
from .models import Product, Category
from .forms import ProductForm, CategoryForm  # Імпорт форм


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


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/product_form.html'  # Використаємо один шаблон для обох
    success_url = reverse_lazy('categories')  # Куди повертати після створення


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products')
