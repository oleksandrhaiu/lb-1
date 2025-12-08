from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),  # Новий

    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),  # Новий
]