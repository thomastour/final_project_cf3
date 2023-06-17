from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly


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
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]  # Prevents users from updating these fields.


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "password",
            "email",
        ]
