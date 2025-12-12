from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# 1. Ця функція спрацює, коли збережеться User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Якщо користувач був створений (а не просто редагувався)
    if created:
        Profile.objects.create(user=instance)

# 2. Ця функція зберігає Профіль, коли зберігається User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()