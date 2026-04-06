from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cook, Dish

class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
        )

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"
        widgets = {
            'cooks': forms.CheckboxSelectMultiple(),
            'ingredients': forms.CheckboxSelectMultiple(),
        }
