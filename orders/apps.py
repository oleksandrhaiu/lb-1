from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders' # Було 'products', стало 'orders' (щоб Django не сварився на дублікати)
