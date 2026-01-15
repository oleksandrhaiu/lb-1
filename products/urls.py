from django.urls import path
from . import views

urlpatterns = [
    # Категорії (було 'categories/', стало 'categories/') - тут ок
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),

    # ТОВАРИ
    # Було 'products/', СТАЛО '' (порожній рядок)
    # Це означає: shop.urls вже дав нам prefix 'products/', тому тут ми просто беремо корінь
    path('', views.ProductListView.as_view(), name='products'),

    # Було 'products/create/', СТАЛО 'create/'
    path('create/', views.ProductCreateView.as_view(), name='product-create'),

    # Було 'products/<int:pk>/', СТАЛО '<int:pk>/'
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    # Було 'products/update/...', СТАЛО 'update/...'
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),

    # Було 'products/delete/...', СТАЛО 'delete/...'
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]