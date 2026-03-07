import datetime
from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

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
    
        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def validate_release_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("The release year cannot be in the future.")
        return value

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
        ]
