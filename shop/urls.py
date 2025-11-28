from django.contrib import admin
from django.urls import path, include # 1. Додано include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')), # 2. Підключено файл маршрутів додатку
]
