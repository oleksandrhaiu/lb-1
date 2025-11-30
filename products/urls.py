from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для категорій: /products/categories/
    path('categories/', views.categories, name='categories'),

    # Маршрут для товарів: /products/products/
    path('products/', views.products, name='products'),
]