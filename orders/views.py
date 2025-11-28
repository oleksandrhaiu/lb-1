from django.http import HttpResponse

def index(request):
    return HttpResponse("Вітаємо! Це сторінка копії додатку - Orders.")