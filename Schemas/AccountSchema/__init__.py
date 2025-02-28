from pydantic import BaseModel, Field
from typing import Optional, Literal

class AccountSchema(BaseModel):
    account_id: Optional[int] = None
    account_number: str = Field(..., min_length=5, max_length=20)
    customer_id: int
    customer_phone_number: str = Field(..., min_length=10, max_length=20)
    account_type: Literal["Savings", "Current"]
    balance: float = Field(..., ge=0)
    date_opened: str = Field(..., min_length=4, max_length=20)
    status: Literal["Active", "Inactive", "Closed"]

    # Savings Account Fields
    interest_rate: Optional[float] = None
    minimum_balance: Optional[float] = None

    # Current Account Fields
    overdraft_limit: Optional[float] = None
    monthly_fee: Optional[float] = None

    class Config:
        orm_mode = True