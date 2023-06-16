from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genre",
            "director",
            "release_year",
            "actor",
            "description",
            "created_at",
            "updated_at",
            "user",
        ]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "password",
            "email",
        ]
