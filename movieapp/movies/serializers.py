import datetime
from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model
#from .permissions import IsOwnerOrReadOnly
#from .models import  CustomUser

# The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
class MovieSerializer(serializers.ModelSerializer):

    user =serializers.StringRelatedField(read_only=True) #to display username instead of id
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
        ]  # Prevents users from updating these fields.

def validate_release_year(value):
    """
    Check that the release year is not in the future.
    """
    if value > datetime.datetime.now().year:
        raise serializers.ValidationError("The release year cannot be in the future.")
    return value

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "password",
            "email",
        ]
