from django.http import HttpResponse
from .models import Category, Product


def index(request):
    # Отримуємо дані з бази
    categories = Category.objects.all()
    products = Product.objects.all()

    # Формуємо рядок відповіді
    response_html = "<h1>Категорії:</h1>"
    response_html += ''.join([f"- {c.title}<br>" for c in categories])

    response_html += "<h1>Товари:</h1>"
    response_html += ''.join([f"- {p.title} (Ціна: {p.price})<br>" for p in products])

    return HttpResponse(response_html)