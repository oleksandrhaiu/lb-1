from django.contrib import admin
from .models import Category, Product

# Реєстрація моделей в адмінці
admin.site.register(Category)
admin.site.register(Product)