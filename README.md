# SWE-team-A

## Endpoints

### Service: Users

- **POST /login**:
    - Request:
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
    - Request:
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
    "redirect_url": "/user/login"
  }
  ```
    - Errors: 409, 422


- **POST /signup/buyer**:
    - Request:
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
    "redirect_url": "/user/login"
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

## Errors

- **401 (Unauthorized) / 403 (Forbidden) / 409 (Conflict) / 422 (Unprocessable Entity)**:
  ```json
  {
    "message": string,
    "details": string,
    "request": dict{"...": "...",...} or null,
    "auth_user": dict{"...": "...",...} or null
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