from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Зв'язок з користувачем (1 користувач = 1 профіль)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Поле для біографії (необов'язкове)
    bio = models.TextField(blank=True)

    # Поле для аватарки
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    # Поле для дати народження (необов'язкове)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"