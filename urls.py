from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Імпорт стандартних вюх
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Підключаємо наші товари (це у тебе вже було)
    path('', include('products.urls')),

    # 1. Підключаємо шляхи нашого нового додатку (реєстрація, профіль)
    path('accounts/', include('accounts.urls')),

    # 2. Стандартний вхід (вказуємо наш шаблон)
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # 3. Стандартний вихід
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]

# Додаємо підтримку медіа-файлів (картинок), якщо включено режим розробки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)