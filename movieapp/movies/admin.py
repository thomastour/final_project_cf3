from django.contrib import admin

from .models import CustomUser
from .models import Movie

admin.site.register(Movie)
admin.site.register(CustomUser)
