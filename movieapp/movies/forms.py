from django import forms
from .models import Movie
from movies.models import CustomUser


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
