# 🛠 API Naming Conventions (RESTful)

Creating a clean and consistent naming convention in your API makes it easier for developers to understand, maintain, and use. Follow these guidelines to build a well-structured RESTful API.

---

- always lowercase letters
- hyper to separate multiple words
- use camelCase for variables and wrap them around {}, for instance `{}`, for instance `/courses/{courseId}`.
- use meaningful words to convey what the API is about.
- use forward slashes `/` to indicate relationships and hierarchical structure.
- use nouns and never verbs, `/books/{bookId}`, not `/getBook/{bookId}`; `/books/{bookId}` and wrong one is `/books/delete`, we should make a request instead of using delete word.
- end api without forward slash at the end, `/books/{bookId}` not `/books/{bookId}/`.
- use Query parameters for data types, in a url, everything after `?` will treated as query string, for instance `/books?author=knight`.

## 📖 Key Principles

### 1️⃣ Always Lowercase Letters

- Use **lowercase** for all paths.
  - ✅ `/users`
  - ❌ `/Users`

---

### 2️⃣ Hyphen to Separate Words

- Use **hyphens** to separate multiple words in URLs.
  - ✅ `/user-profiles`
  - ❌ `/userProfiles`

---

### 3️⃣ Use CamelCase for Variables

- Wrap variables in curly braces `{}` and use **camelCase** for naming.
  - ✅ `/courses/{courseId}`
  - ❌ `/courses/{course_id}`

---

### 4️⃣ Meaningful Words

- Use descriptive and meaningful nouns to convey the purpose of the API.
  - ✅ `/products/{productId}`
  - ❌ `/stuff/{id}`

---

### 5️⃣ Use Forward Slashes for Hierarchy

- Use `/` to indicate relationships and hierarchy in resources.
  - ✅ `/users/{userId}/orders/{orderId}`
  - ❌ `/users-orders`

---

### 6️⃣ Use Nouns, Not Verbs

- The resource name should be a **noun** (not an action or verb).
  - ✅ `/books/{bookId}`
  - ❌ `/getBook/{bookId}`
  - ✅ `DELETE /books/{bookId}` (use HTTP method for the action).
  - ❌ `/books/delete/{bookId}`

---

### 7️⃣ No Trailing Slash

- Avoid ending a URL with a forward slash `/`.
  - ✅ `/books/{bookId}`
  - ❌ `/books/{bookId}/`

---

### 8️⃣ Query Parameters for Filtering & Search

- Use query strings for operations like filtering, searching, and sorting.
  - ✅ `/books?author=knight`
  - ❌ `/books/author/knight`

---

## 📖 Examples

| **Action**                | **Endpoint**                       | **HTTP Method** |
| ------------------------- | ---------------------------------- | --------------- |
| Retrieve all books        | `/books`                           | `GET`           |
| Retrieve a specific book  | `/books/{bookId}`                  | `GET`           |
| Add a new book            | `/books`                           | `POST`          |
| Update a book             | `/books/{bookId}`                  | `PUT`           |
| Delete a book             | `/books/{bookId}`                  | `DELETE`        |
| Get books by author       | `/books?author=knight`             | `GET`           |
| Get user orders           | `/users/{userId}/orders`           | `GET`           |
| Get a specific user order | `/users/{userId}/orders/{orderId}` | `GET`           |

---

## 🚀 Final Checklist

- ✅ Use **lowercase** for all paths.
- ✅ Separate words with **hyphens**.
- ✅ Wrap variables in `{}` and use **camelCase** for variables.
- ✅ Use **nouns** and HTTP methods for actions.
- ✅ Avoid trailing slashes `/` at the end of URLs.
- ✅ Use **query parameters** for filtering, searching, or sorting.

By following these conventions, your RESTful API will be clean, intuitive, and easy to maintain!

## 🌟 General Best Practices

- **Use kebab-case or snake_case for URLs**: Consistent casing improves readability.

  - ✅ `GET /user-profiles` (Preferred)
  - ❌ `GET /UserProfiles` (Avoid)

- **Stick to HTTP Methods**: Let the HTTP method (e.g., `GET`, `POST`) define the action, not the endpoint name.

  - ✅ `POST /users` (to create a user)
  - ❌ `POST /createUser` (Avoid)

- **Pluralize resource names**: Use plurals for resource collections.
  - ✅ `/users` (Preferred)
  - ❌ `/user` (Avoid unless dealing with a single resource like `/me`).

---

## 🔑 Key Endpoints & Structure

### 1️⃣ CRUD Operations

Use standard HTTP methods for CRUD operations:  
| HTTP Method | Purpose | Example |
|-------------|------------------------|----------------------|
| `GET` | Retrieve data | `GET /users` |
| `POST` | Create a new resource | `POST /users` |
| `PUT` | Update an entire resource | `PUT /users/123` |
| `PATCH` | Partially update a resource | `PATCH /users/123`|
| `DELETE` | Remove a resource | `DELETE /users/123` |

---

### 2️⃣ Nested Resources

Use nested routes for relationships:

- ✅ `GET /users/123/orders` (Retrieve orders of user 123).
- ✅ `POST /users/123/orders` (Add a new order for user 123).

---

### 3️⃣ Filtering, Sorting, and Pagination

- **Filtering**: Use query parameters.
  - ✅ `GET /users?role=admin` (Filter users by role).
- **Sorting**: Use a `sort` parameter.
  - ✅ `GET /users?sort=created_at`
- **Pagination**: Use `page` and `limit`.
  - ✅ `GET /users?page=1&limit=20`

---

### 4️⃣ Action Endpoints

For non-CRUD actions, use meaningful names while keeping them resource-oriented:

- ✅ `POST /users/123/reset-password`
- ✅ `POST /orders/123/cancel`
- ❌ `POST /resetUserPassword` (Avoid)

---

## 📖 Example API Design

### User Resource

| Action                 | Endpoint                    | HTTP Method |
| ---------------------- | --------------------------- | ----------- |
| Retrieve all users     | `/users`                    | `GET`       |
| Retrieve a single user | `/users/123`                | `GET`       |
| Create a new user      | `/users`                    | `POST`      |
| Update a user          | `/users/123`                | `PUT`       |
| Delete a user          | `/users/123`                | `DELETE`    |
| Reset user password    | `/users/123/reset-password` | `POST`      |

---

### Pro Tip 💡

Use **consistent error responses** (e.g., HTTP codes and JSON structures):

- `404 Not Found`: When a resource doesn’t exist.
- `400 Bad Request`: When input data is invalid.
- `500 Internal Server Error`: For unexpected server issues.

---

A well-designed RESTful API follows predictable patterns, reducing the learning curve for developers. Consistency is key!
