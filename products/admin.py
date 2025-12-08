from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Поля, які видно в списку
    list_display = ('title', 'category', 'price', 'product_qty', 'created_at')

    # Поля, за якими можна фільтрувати (бокова панель справа)
    list_filter = ('category', 'created_at')

    # Поля, які можна редагувати прямо в списку
    # Важливо: перше поле (title) зазвичай є посиланням, тому його редагувати не можна
    list_editable = ('price', 'product_qty')