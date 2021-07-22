# Socian Network REST API

### Framework

Django Rest Framework </br>

### Endpoints

| Endpoint | Description |
| --- | --- |
| " " | Home page; the list of posts |
| "id/" | Detail view of the post |
| "create/" | Create new post |
| "update/id/" | Update or Delete the post |
| "auth/users/" | Register a new user |
| "api/token/" | Create a JWT by passing a valid user in the post request to this endpoint |
| "api/token/refresh/" | Get a new JWT once the lifetime of the previously generated one expires |

### Models
* User
* Post

### Features
* User signup
* User login
* Post Create/Read/Update/Delete
* JSON Web Token (JWT) authentification
