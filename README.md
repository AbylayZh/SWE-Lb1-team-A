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