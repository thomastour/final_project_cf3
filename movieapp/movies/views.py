from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .forms import CustomUserCreationForm, MovieForm
from .serializers import MovieSerializer
from rest_framework.views import APIView



class MovieList(APIView):
    """
    API endpoint to get all movies or create a new movie.
    """

    def get(self, request):
        """
        Retrieve all movies.
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new movie.
        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    """
    API endpoint to retrieve, update, or delete a specific movie.
    """


    def get(self, request, pk):
        """
        Retrieve a specific movie by ID.
        """
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific movie by ID.
        """
        movie = get_object_or_404(Movie, pk=pk) 
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific movie by ID.
        """
        movie = get_object_or_404(Movie, pk=pk)
        self.check_object_permissions(request, movie)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



def home_view(request):
    """
    Render the home page.
    """
    return render(request, "movies/home.html")


def login_view(request):
    """
    Handle user login.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # Create a form instance with the submitted data
        if form.is_valid(): # Check if the form is valid
            username = form.cleaned_data.get("username") # Get the username from the form
            password = form.cleaned_data.get("password") # Get the password from the form
            print(f"Username: {username}, Password: {password}") 

            user = authenticate(request, username=username, password=password) # Authenticate the user
            if user is not None: # Check if the user was authenticated successfully
                print("Authentication successful")
                login(request, user)
                return redirect("menu")
            else:
                print("Authentication failed")
                error_message = "Authentication failed. Invalid username or password" # If the user was not authenticated successfully, display an error message
                return render(
                    request,
                    "movies/login.html",
                    {"form": form, "error_message": error_message},
                )
        else:
            error_message = "form is invalid" #refers to errors related to the overall form structure or format, such as missing required fields, incorrect field types
            print("Form is invalid")
            print(form.errors)
    else:
        form = AuthenticationForm(request) 

    return render(request, "movies/login.html", {"form": form})


def register_view(request):
    """
    Handle user registration.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(
                commit=False
            )  # Create a new user object but don't save it yet
            password = form.cleaned_data.get(
                "password"
            )  # Get the password from the form
            user.password = make_password(password)  # Hash the password
            user.save()
            login(request, user)
            return redirect("menu")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(
        request, "movies/register.html", {"form": form, "registration_success": False}
    )


def menu_view(request):
    if request.method == "POST":
        if "logout" in request.POST:
            logout(request)

    return render(request, "movies/menu.html")


def movie_list_view(request):
    """
    Render the movie list page with the option to filter movies based on search criteria.
    """
    movies = Movie.objects.all()

    # Filter movies based on search criteria
    title = request.GET.get("title")
    genre = request.GET.get("genre")
    director = request.GET.get("director")
    release_year = request.GET.get("release_year")

    if title:
        movies = movies.filter(title__icontains=title)
    if genre:
        movies = movies.filter(genre__icontains=genre)
    if director:
        movies = movies.filter(director__icontains=director)
    if release_year:
        movies = movies.filter(release_year=release_year)

    if request.method == "POST":
        if "logout" in request.POST:
            logout(request)
            return redirect(reverse("login"))

    context = {
        "movies": movies,
        "searched": any([title, genre, director, release_year]),
    }

    return render(request, "movies/movie_list.html", context)


def movie_detail_view(request, pk):
    """
    Render the movie detail page for a specific movie.
    """
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movies/movie_detail.html", {"movie": movie})


def movie_create_view(request):
    """
    Render the movie creation form and handle the creation of a new movie.
    """
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()
    return render(request, "movies/movie_create.html", {"form": form})


def movie_update_view(request, pk):
    """
    Render the movie update form and handle the update of an existing movie.
    """
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm(instance=movie)
    return render(request, "movies/movie_update.html", {"form": form, "movie": movie})




def movie_delete_view(request, pk):
    """
    Render the movie delete confirmation page and handle the deletion of a movie.
    """
    movie = get_object_or_404(Movie, pk=pk) 
    if request.method == "POST": # Check if the request method is POST
        if request.user == movie.user: # Check if the user is the owner of the movie
            movie.delete() # Delete the movie
        return redirect("movie_list") 
    
    return render(request, "movies/movie_delete.html", {"movie": movie})
