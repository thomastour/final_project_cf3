from django.contrib import admin
from django.urls import path
from movies import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("menu/", views.menu_view, name="menu"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("movies/", views.movie_list_view, name="movie_list"),
    path("movies/<int:pk>/", views.movie_detail_view, name="movie_detail"),
    path("movies/create/", views.movie_create_view, name="movie_create"),
    path("movies/<int:pk>/update/", views.movie_update_view, name="movie_update"),
    path("movies/<int:pk>/delete/", views.movie_delete_view, name="movie_delete"),
    # API views
    path("api/movies/", views.MovieList.as_view(), name="api_movie_list"),
    path("api/movies/<int:pk>/", views.MovieDetail.as_view(), name="api_movie_detail"),
]
