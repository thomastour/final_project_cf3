Movie API
=========

This API allows you to perform CRUD operations (Create, Read, Update, Delete) on movies.

Base URL
--------
The base URL for accessing the Movie API is: `http://example.com/api/movies/`

Authentication
--------------
Authentication is required to access certain endpoints.

Endpoints
---------
1. Retrieve All Movies
    - URL: `/api/movies/`
    - Method: GET
    - Description: Retrieve a list of all movies.
    - Authentication Required: No
    - Response:
        - Success: Status 200 OK
        - Content: JSON object containing a list of movies and their details.

2. Create a New Movie
    - URL: `/api/movies/`
    - Method: POST
    - Description: Create a new movie.
    - Authentication Required: Yes
    - Request Body: JSON object containing the details of the movie to be created.
    - Response:
        - Success: Status 201 Created
        - Content: JSON object containing the details of the created movie.

3. Retrieve a Specific Movie
    - URL: `/api/movies/{movie_id}/`
    - Method: GET
    - Description: Retrieve details for a specific movie.
    - Authentication Required: No
    - Response:
        - Success: Status 200 OK
        - Content: JSON object containing the details of the specified movie.
        - Error: Status 404 Not Found if the movie does not exist.

4. Update a Specific Movie
    - URL: `/api/movies/{movie_id}/`
    - Method: PUT
    - Description: Update details for a specific movie.
    - Authentication Required: Yes
    - Request Body: JSON object containing the updated details of the movie.
    - Response:
        - Success: Status 200 OK
        - Content: JSON object containing the updated details of the movie.
        - Error: Status 404 Not Found if the movie does not exist.

5. Delete a Specific Movie
    - URL: `/api/movies/{movie_id}/`
    - Method: DELETE
    - Description: Delete a specific movie.
    - Authentication Required: Yes
    - Response:
        - Success: Status 204 No Content
        - Error: Status 404 Not Found if the movie does not exist.

Example Usage
-------------
1. Retrieve All Movies
    - Request:
        ```
        GET /api/movies/
        ```
    - Response:
        ```
        Status: 200 OK
        Content-Type: application/json

        [
            {
                "id": 1,
                "title": "Movie 1",
                "genre": "Action",
                "director": "Director 1",
                "release_year": 2021,
                "actor": "Actor 1",
                "actress": "Actress 1"
                "description": "Description 1",
                "created_at": "2021-01-01T00:00:00Z",
                "updated_at": "2021-01-01T00:00:00Z",
                "user": 1
            },
            {
                "id": 2,
                "title": "Movie 2",
                "genre": "Drama",
                "director": "Director 2",
                "release_year": 2022,
                "actor": "Actor 2",
                "actress": "Actress 2"
                "description": "Description 2",
                "created_at": "2021-02-01T00:00:00Z",
                "updated_at": "2021-02-01T00:00:00Z",
                "user": 2
            },
            ...
        ]
        ```

2. Create a New Movie
    - Request:
        ```
        POST /api/movies/
        Content-Type: application/json
        Authorization: Bearer {access_token}

        {
            "title": "New Movie",
            "genre": "Comedy",
            "director": "Director 3",
            "release_year": 2023
        }
        ```
    - Response:
        ```
        Status: 201 Created
        Content-Type: application/json

        {
            "id": 3,
            "title": "New Movie",
            "genre": "Comedy",
            "director": "
        }
        ```