from pydantic import BaseModel, Field
from typing import Optional

class CustomerSchema(BaseModel):
    customer_id: Optional[int] = None
    name: str = Field(..., min_length=2, max_length=50)
    dob: str = Field(..., min_length=10, max_length=20)
    city: str = Field(..., min_length=2, max_length=100)
    pincode: str = Field(..., min_length=4, max_length=10)
    phone_number: str = Field(..., min_length=10, max_length=20)
    email: str = Field(..., min_length=5, max_length=50)
    aadhar_number: str = Field(..., min_length=12, max_length=20)

    class Config:
        orm_mode = True