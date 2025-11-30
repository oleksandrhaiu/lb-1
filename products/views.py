from django.http import HttpResponse
from .models import Category

def index(request):
    categories = Category.objects.all()
    return HttpResponse(''.join([str(category) + '<br>' for category in categories]))