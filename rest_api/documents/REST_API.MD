## Application Programming Interface (API)

It is gate to backend data and it allows to access and modify these data.

## RESTful API

It is an architectural design to create the APIs for our project.
they provide an easy way to communicate with sever and access the data that powers our application.

an API is RESTful if it follow certain standards, here are the most important ones.

- It must have client-server architecture
- alway stateless
- should be cacheable
- it should be layered
- it should have a uniform interface

#### 1. client-server architecture

a client-server architecture contains a server to provide the resources and a client to consume them.

#### 2. stateless

it means server does not have any any info about state of the API client who is making the call and it cannot identify who is making the request or what their previously requested data was.
in fact, state is only save on client machine not on the server.

#### 3. cacheable

the response should be savable on browser or server and it helps to reduce the server load by using the saved response instead of making a new request.

#### 4. layered

it should have different layers and those layers are removable any time.

the layers could be

```
|Client| --> |Firewall| --> |Load balancer| --> |web server| --> |database server|
```

#### 5. Uniform interface

it means the system should offer a uniform interface to access the resource, for instance, there should be unique `URL` for each resource.

## Naming convention

- always lowercase letters
- hyper to separate multiple words
- use camelCase for variables and wrap them around {}, for instance `{}`, for instance `/courses/{courseId}`.
- use meaningful words to convey what the API is about.
- use forward slashes `/` to indicate relationships and hierarchical structure.
- use nouns and never verbs, `/books/{bookId}`, not `/getBook/{bookId}`, `/books/{bookId}` and wrong one is `/books/delete`, we should make a request instead of using delete word.
- end api without forward slash at the end, `/books/{bookId}` not `/books/{bookId}/`.
- use Query parameters for data types, in a url, everything after `?` will treated as query string, for instance `/books?author=knight`.

### Tools

- `curl https://www.coursera.org/learn/apis/lecture/GfIq7/essential-tools-for-api-development` can be used to make get request from a terminal.
