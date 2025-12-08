from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # --- НОВЕ: Налаштування відображення ---
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    # --- НОВЕ: Налаштування відображення ---
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['title']