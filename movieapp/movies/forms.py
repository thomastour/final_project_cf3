from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "genre", "director", "release_year", "actor", "description"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
