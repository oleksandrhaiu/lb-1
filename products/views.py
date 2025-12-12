from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
# 1. Імпорт міксина для захисту
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Category
from .forms import ProductForm, CategoryForm

# --- READ (Перегляд доступний всім) ---

class CategoryListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    ordering = ['title']

class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['-created_at']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

# --- CREATE, UPDATE, DELETE (Тільки для авторизованих) ---

# Додаємо LoginRequiredMixin першим у дужках!

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('categories')
    login_url = '/login/'  # Куди перенаправляти, якщо не увійшов

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products')
    login_url = '/login/'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products')
    login_url = '/login/'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products')
    login_url = '/login/'