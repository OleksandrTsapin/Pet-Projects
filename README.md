# Socian Network REST API


### Endpoints

" " &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> Home page; the list of posts

"id/" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> Detail view of the post

"create/" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> Create new post

"update/id/" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> Update or Delete the post

"auth/users/" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> Register a new user

"api/token/" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --> create a JWT by passing a valid user in the post request to this endpoint

"api/token/refresh/" --> get a new JWT once the lifetime of the previously generated one expires
