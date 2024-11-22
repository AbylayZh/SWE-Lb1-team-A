# SWE-team-A

## Admin Credentials

```json
{
  "email": "admin@mail.com",
  "password": "12345"
}
 ```

## Endpoints

### Service: Users

- **POST /login**:
    - Request (JSON):
  ```json
  {
    "email": string,
    "password": string
  }
  ```
    - Response (303 Redirect):
  ```json
  {
    "message": "OK",
    "redirect_url": "/"
  }
  ```
    - Errors: 401


- **POST /signup/farmer**:
    - Request (JSON):
  ```json
  {
    "first_name": string,
    "last_name": string,
    "email": string,
    "phone": int,
    "password": string,
    "farm_size": int,
    "farm_address": string
  }
  ```
    - Response (303 Redirect):
  ```json
  {
    "message": "OK",
    "redirect_url": "/login"
  }
  ```
    - Errors: 409, 422


- **POST /signup/buyer**:
    - Request (JSON):
  ```json
  {
    "first_name": string,
    "last_name": string,
    "email": string,
    "phone": int,
    "password": string,
    "delivery_address": str,
    "preferred_payment": int
  }
  ```
    - Response (303 Redirect):
  ```json
  {
    "message": "OK",
    "redirect_url": "/login"
  }
  ```
    - Errors: 409, 422


- **POST /user/logout**:
    - Request: None
    - Response (303 Redirect):
  ```json
  {
    "message": "OK",
    "redirect_url": "/"
  }
  ```

### Service: Admin

- **GET /user/role/admin/users/pending**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "unapproved_users": List[dict{"first_name": "...", "last_name": "...", ...}]
  }
  ```

- **GET /user/role/admin/users/active**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "active_users": List[dict{"first_name": "...", "last_name": "...", ...}]
  }
  ```

- **GET /user/role/admin/users/inactive**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "inactive_users": List[dict{"first_name": "...", "last_name": "...", ...}]
  }
  ```

- **GET /user/role/admin/users/{id}**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "user": dict{"first_name": "...", "last_name": "...", ...}
  }
  ```

- **DELETE "/user/role/admin/users/delete/{id}"**:
    - Request: None
    - Response (303 Redirect):
  ```json
  {
    "message": "OK", 
    "redirect_url": "/user/role/admin/users/pending"
  }
  ```

- **PUT /user/role/admin/users/approve/{id}**:
    - Request: None
    - Response (303 Redirect):
  ```json
  {
    "message": "OK", 
    "redirect_url": "/user/role/admin/users/pending"
  }
  ```

- **PUT /user/role/admin/users/enable/{id}**:
    - Request: None
    - Response (303 Redirect):
  ```json
  {
    "message": "OK", 
    "redirect_url": "/user/role/admin/users/inactive"
  }
  ```

- **PUT /user/role/admin/users/disable/{id}**:
    - Request: None
    - Response (303 Redirect):
  ```json
  {
    "message": "OK", 
    "redirect_url": "/user/role/admin/users/active"
  }
  ```

### Service: Farmers / Products

- **GET /user/role/farmer/products**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "products": List[dict{"id": "...", "name": "...", "description": "...", ...}]
  }
  ```

- **POST /user/role/farmer/products/create**:
    - Request (form-data):
  ```json
  {
    "name": string,
    "description": string,
    "price": int,
    "category_id": int,
    "quantity": int,
    "weight": float,
    "files": List[file_type]
  }
  ```
    - Response (303 Redirect):
  ```json
  {
    "message": "OK",
    "redirect_url": "/user/role/farmer/products/{product_id}",
    "authenticated_user": dict{"first_name": "...", "last_name": "...", ...} or null
  }
  ```

- **GET /user/role/farmer/products/{id}**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "product": dict{"id": "...", "name": "...", "description": "...", ...}, 
    "images": List[image{"id": "...", "path": "...", ...}]
  }
  ```

- **DELETE /user/role/farmer/products/delete/{id}**:
    - Request: None
    - Response (303 Redirect):
  ```json
  {
    "message": "OK", 
    "redirect_url": "/user/role/farmer/products"
  }
  ```

### Service: Buyers / Products

- **GET /user/role/buyer/products**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "products": List[dict{"id": "...", "name": "...", "description": "...", ...}]
  }
  ```

- **GET /user/role/buyer/products/{id}**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "product": dict{"id": "...", "name": "...", "description": "...", ...}, 
    "images": List[image{"id": "...", "path": "...", ...}]
  }
  ```

## Errors

- **401 (Unauthorized) / 403 (Forbidden) / 409 (Conflict) / 422 (Unprocessable Entity)**:
  ```json
  {
    "message": string,
    "details": string,
    "request": dict{"...": "...", ...} or null,
    "authenticated_user": dict{"first_name": "...", "last_name": "...", ...} or null
  }
  ```

- **404 (Not Found) / 405 (Method Not Allowed)**:
  ```json
  {
    "detail": string
  }
  ```

- **500 (Internal Server)**:
  ```json
  {
    "message": string,
    "details": string
  }
  ```