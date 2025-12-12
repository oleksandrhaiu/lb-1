from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# 1. Форма реєстрації (розширюємо стандартну, додаючи Email)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
        # Паролі Django додасть автоматично завдяки UserCreationForm

# 2. Форма оновлення даних користувача (Логін, Email)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# 3. Форма оновлення профілю (Картинка, Біо, Дата)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'birth_date']
        # Можна додати віджети для краси (наприклад, календар для дати),
        # але поки зробимо базово, як у завданні.