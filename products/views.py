from django.shortcuts import render
from .models import Category, Product

# Обробник для сторінки категорій
def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'products/categories.html', {'categories': categories_list})

# Обробник для сторінки товарів
def products(request):
    products_list = Product.objects.all()
    return render(request, 'products/products.html', {'products': products_list})