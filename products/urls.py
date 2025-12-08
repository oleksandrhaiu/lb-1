from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),

    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),

    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),

    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]
