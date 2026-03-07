import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import CustomUserCreationForm, MovieForm
from .models import Movie


class MovieFormTests(TestCase):
    def test_movie_form_does_not_expose_user_field(self):
        self.assertNotIn("user", MovieForm().fields)


class RegistrationFormTests(TestCase):
    def test_registration_requires_matching_passwords(self):
        form = CustomUserCreationForm(
            data={
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "StrongPass123",
                "password2": "Mismatch123",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class MovieViewTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.owner = self.user_model.objects.create_user(
            username="owner",
            email="owner@example.com",
            password="StrongPass123",
        )
        self.other_user = self.user_model.objects.create_user(
            username="other",
            email="other@example.com",
            password="StrongPass123",
        )
        self.movie = Movie.objects.create(
            title="Existing movie",
            genre="Drama",
            director="Director",
            release_year=2020,
            actor="Actor",
            description="Original description",
            user=self.owner,
        )

    def test_create_view_assigns_logged_in_user(self):
        self.client.force_login(self.owner)

        response = self.client.post(
            reverse("movie_create"),
            data={
                "title": "New movie",
                "genre": "Sci-fi",
                "director": "Director",
                "release_year": 2022,
                "actor": "Actor",
                "description": "Created in test",
            },
        )

        self.assertRedirects(response, reverse("movie_list"))
        created_movie = Movie.objects.get(title="New movie")
        self.assertEqual(created_movie.user, self.owner)

    def test_update_view_blocks_non_owner(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse("movie_update", args=[self.movie.pk]),
            data={
                "title": "Changed title",
                "genre": self.movie.genre,
                "director": self.movie.director,
                "release_year": self.movie.release_year,
                "actor": self.movie.actor,
                "description": self.movie.description,
            },
        )

        self.assertEqual(response.status_code, 403)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Existing movie")

    def test_api_update_blocks_non_owner(self):
        self.client.force_login(self.other_user)

        response = self.client.put(
            reverse("api_movie_detail", args=[self.movie.pk]),
            data=json.dumps(
                {
                    "title": "Changed from api",
                    "genre": self.movie.genre,
                    "director": self.movie.director,
                    "release_year": self.movie.release_year,
                    "actor": self.movie.actor,
                    "description": self.movie.description,
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 403)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Existing movie")
