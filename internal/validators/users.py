from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: int
    password: str


class FarmerSignupRequest(SignupRequest):
    farm_size: int
    farm_address: str


class BuyerSignupRequest(SignupRequest):
    delivery_address: str
    preferred_payment: int
