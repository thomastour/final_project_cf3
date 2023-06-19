# final_project_cf3
## MOVIEPEDIA

**MOVIEPEDIA** is a comprehensive movie database and information platform developed using Python and Django. It allows users to explore, search, and contribute to a vast collection of movies. Whether you're a movie enthusiast, a film critic, or simply looking for information about a specific movie, MOVIEPEDIA has you covered.

**Key Features**

- User Registration and Login: Create an account and securely log in to MOVIEPEDIA to unlock additional features and contribute to the platform.

- Movie Management: Contribute to the platform by adding new movies, updating movie descriptions, and deleting movies if necessary.

- Advanced Search: Easily find movies using various search criteria such as actors, genre, directors, or release year.

- Responsive Design: The user interface is built with Bootstrap, ensuring a seamless and visually appealing experience across different devices.


**Technologies Used:**
``` 
    Python
    Django
    SQLite
    HTML
    Bootstrap
```

**Installation**
To get started with MOVIEPEDIA, follow these steps:

- Clone the MOVIEPEDIA repository to your local machine.
  ```
  git clone https://github.com/your-username/MOVIEPEDIA.git
```
- Install the required Python dependencies using pip.

```
cd MOVIEPEDIA
pip install -r requirements.txt
```
- Set up the database and apply migrations.
```
python manage.py migrate
```
- Start the Django development server.
```
python manage.py runserver
```
  
- Access MOVIEPEDIA through your preferred web browser.
```
http://localhost:8000/
```

- Register an account or log in to begin exploring, contributing, and searching for movies.

**API Endpoints**
MoviePedia provides the following API endpoints for programmatic access:

- GET /api/movies/: Retrieve a list of all movies.
- POST /api/movies/: Create a new movie.
- GET /api/movies/{movie_id}/: Retrieve details for a specific movie.
- PUT /api/movies/{movie_id}/: Update details for a specific movie.
- DELETE /api/movies/{movie_id}/: Delete a specific movie.
- Please note that authentication is required for certain endpoints.

For detailed information about the API and available request/response formats, refer to the [![API Documentation](https://img.shields.io/badge/API-Documentation-blueviolet)](./API_documentation.md)


**Contributing**
We welcome contributions from the open-source community to enhance MOVIEPEDIA. If you find any bugs, have feature requests, or want to contribute code, please follow our Contribution Guidelines.

**License**
MOVIEPEDIA is released under the MIT License. You are free to use, modify, and distribute this project as per the terms of the license.

<h2>Home Page</h2>
  <img src="/moviepedia%20img/home.JPG" alt="home page" width="700" height="500">

<h2>Login Page</h2>
  <img src="/moviepedia%20img/login.JPG" alt="Login page" width="500" height="500">

<h2>Registration Page</h2>
  <img src="/moviepedia%20img/register.JPG" alt="registration page" width="500" height="500">

  <h2>Menu</h2>
  <img src="/moviepedia%20img/menu.JPG" alt="menu page" width="500" height="500">

  <h2>Movie List Page</h2>
  <img src="/moviepedia%20img/movie_list.JPG" alt="movie list" width="700" height="600">

  <h2>Movie Detail Page</h2>
  <img src="/moviepedia%20img/movie_detail.JPG" alt="movie detail page" width="700" height="600">

  <h2>Movie Edit/Update Page</h2>
  <img src="/moviepedia%20img/update_edit.JPG" alt="update_edit page" width="500" height="500">

  <h2>Delete Page</h2>
  <img src="/moviepedia%20img/delete.JPG" alt="delete page" width="500" height="500">
