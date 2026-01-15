from django import forms

# Створюємо список цифр від 1 до 20 [(1, '1'), (2, '2')...]
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int, # Перетворює вибір користувача в число (int)
        label='Кількість'
    )
    # Це приховане поле. Якщо True - ми перезаписуємо кількість, якщо False - додаємо (+1)
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )