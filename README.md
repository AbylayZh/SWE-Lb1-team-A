# SWE-team-A

## How to use:

Link to the API (Render): [https://swe-lb1-team-a.onrender.com](https://swe-lb1-team-a.onrender.com)

Or...

1. Clone repo:
```shell
git clone https://github.com/itelman/farmer-market-system.git
```

2. Open repo:
```shell
cd ./farmer-market-system
```

3. Run the repo:
```shell
fastapi dev main.py
```

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
    "email": "string",
    "password": "string"
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
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "phone": "int",
    "password": "string",
    "farm_size": "int",
    "farm_address": "string"
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
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "phone": "int",
    "password": "string",
    "delivery_address": "string",
    "preferred_payment": "int"
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
    "unapproved_users": [
      {
        "id": "int",
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "phone": "int",
        "created": "datetime",
        "approved": "int",
        "active": "int",
        "role": "string"  
      }
    ]
  }
  ```

- **GET /user/role/admin/users/active**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "active_users": [
        {
          "id": "int",
          "first_name": "string",
          "last_name": "string",
          "email": "string",
          "phone": "int",
          "created": "datetime",
          "approved": "int",
          "active": "int",
          "role": "string"
        }  
    ]
  }
  ```

- **GET /user/role/admin/users/inactive**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "inactive_users": [
        {
          "id": "int",
          "first_name": "string",
          "last_name": "string",
          "email": "string",
          "phone": "int",
          "created": "datetime",
          "approved": "int",
          "active": "int",
          "role": "string"
        }  
    ]
  }
  ```

- **GET /user/role/admin/users/{id}**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "user": {
          "id": "int",
          "first_name": "string",
          "last_name": "string",
          "email": "string",
          "phone": "int",
          "created": "datetime",
          "approved": "int",
          "active": "int",
          "role": "string"
        }  
    
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
    "products": [
      {
        "id": "int", 
        "farmer_id": "int", 
        "name": "string", 
        "description": "string",
        "price": "int",
        "category_id": "int",
        "quantity": "int",
        "weight": "float",
        "created": "datetime"
      }
    ]
  }
  ```

- **POST /user/role/farmer/products/create**:
    - Request (form-data):
  ```json
  {
    "name": "string",
    "description": "string",
    "price": "int",
    "category_id": "int",
    "quantity": "int",
    "weight": "float",
    "files": ["file_type"]
  }
  ```
    - Response (303 Redirect):
  ```json
  {
    "message": "OK",
    "redirect_url": "/user/role/farmer/products/{product_id}",
    "authenticated_user": {
          "id": "int",
          "first_name": "string",
          "last_name": "string",
          "email": "string",
          "phone": "int",
          "created": "datetime",
          "approved": "int",
          "active": "int",
          "role": "string"
        } or null
  }
  ```

- **GET /user/role/farmer/products/{id}**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "product": {
        "id": "int", 
        "farmer_id": "int", 
        "name": "string", 
        "description": "string",
        "price": "int",
        "category_id": "int",
        "quantity": "int",
        "weight": "float",
        "created": "datetime"
      }, 
    "images": [{"id": "int", "path": "string", "created":  "datetime"}]
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
    "products": [
      {
        "id": "int", 
        "farmer_id": "int", 
        "name": "string", 
        "description": "string",
        "price": "int",
        "category_id": "int",
        "quantity": "int",
        "weight": "float",
        "created": "datetime"
      }
    ]
  }
  ```

- **GET /user/role/buyer/products/{id}**:
    - Request: None
    - Response (200 OK):
  ```json
  {
    "product": {
        "id": "int", 
        "farmer_id": "int", 
        "name": "string", 
        "description": "string",
        "price": "int",
        "category_id": "int",
        "quantity": "int",
        "weight": "float",
        "created": "datetime"
      }, 
    "images": [{"id": "int", "path": "string", "created":  "datetime"}]
  }
  ```

## Errors

- **401 (Unauthorized) / 403 (Forbidden) / 409 (Conflict) / 422 (Unprocessable Entity)**:
  ```json
  {
    "message": "string",
    "details": "string" or {"...": "...", ...},
    "request": {"...": "...", ...} or null,
    "authenticated_user": {
          "first_name": string,
          "last_name": string,
          "email": string,
          "phone": int,
          "created": datetime,
          "approved": int,
          "active": int,
          "role": string
        } or null
  }
  ```

- **404 (Not Found) / 405 (Method Not Allowed)**:
  ```json
  {
    "detail": "string"
  }
  ```

- **500 (Internal Server)**:
  ```json
  {
    "message": "string",
    "details": "string"
  }
  ```
