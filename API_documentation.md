**API Documentation**
Movie List [/api/movies/]
Retrieve All Movies [GET]
Retrieves a list of all movies.
Response 200 (application/json)

```
{
"id": 1,
"title": "Pumping Iron",
"genre": "Documentary",
"director": "George Butler - Robert Fiore",
"release_year": 1987,
"actor": "Arnold Schwarzenegger",
"description": "Arnold Schwarzenegger and Lou Ferrigno face off in a no-holds-barred competition for the title of Mr. Olympia in this critically-acclaimed film that made Schwarzenegger a household name.",
"created_at": "2023-06-16T12:18:20.489815Z",
"updated_at": "2023-06-16T12:30:46.794674Z"
}
```

Create a New Movie [POST]
Creates a new movie.

Request (application/json)

````
{
"title": "Pumping Iron",
"genre": "Documentary",
"director": "George Butler - Robert Fiore",
"release_year": 1987,
"actor": "Arnold Schwarzenegger",
"description": "Arnold Schwarzenegger and Lou Ferrigno face off in a no-holds-barred competition for the title of Mr. Olympia in this critically-acclaimed film that made Schwarzenegger a household name."
}
```

Response 201 (application/json)

```
{
"id": 1,
"title": "Pumping Iron",
"genre": "Documentary",
"director": "George Butler - Robert Fiore",
"release_year": 1987,
"actor": "Arnold Schwarzenegger",
"description": "Arnold Schwarzenegger and Lou Ferrigno face off in a no-holds-barred competition for the title of Mr. Olympia in this critically-acclaimed film that made Schwarzenegger a household name.",
"created_at": "2023-06-16T12:18:20.489815Z",
"updated_at": "2023-06-16T12:30:46.794674Z"
}
```

Movie Detail [/api/movies/{id}/]
Retrieve a Specific Movie [GET]
Retrieves a specific movie by its ID.

Parameters

id (number) - ID of the Movie
Response 200 (application/json)


```
{
"id": 1,
"title": "Pumping Iron",
"genre": "Documentary",
"director": "George Butler - Robert Fiore",
"release_year": 1987,
"actor": "Arnold Schwarzenegger",
"description": "Arnold Schwarzenegger and Lou Ferrigno face off in a no-holds-barred competition for the title of Mr. Olympia in this critically-acclaimed film that made Schwarzenegger a household name.",
"created_at": "2023-06-16T12:18:20.489815Z",
"updated_at": "2023-06-16T12:30:46.794674Z"
}
```


Update a Specific Movie [PUT]
Updates a specific movie by its ID.

Parameters

id (number) - ID of the Movie
Request (application/json)


```
{
"title": "Updated Title",
"genre": "Updated Genre",
"director": "Updated Director",
"release_year": 2022,
"actor": "Updated Actor",
"description": "Updated Description"
}
```

Response 200 (application/json)


```
{
"id": 1,
"title": "Updated Title",
"genre": "Updated Genre",
"director": "Updated Director",
"release_year": 2022,
"actor": "Updated Actor",
"description": "Updated Description",
"created_at": "2023-06-16T12:18:20.489815Z",
"updated_at": "2023-06-16T12:30:46.794674Z"
}
```

Delete a Specific Movie [DELETE]
Deletes a specific movie by its ID.

Parameters

id (number) - ID of the Movie
Response 204 (No Content)

Note: Replace {id} in the URL with the actual ID of the movie you want to retrieve, update, or delete.

