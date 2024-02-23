from pydantic import BaseModel, Field
from typing import Optional

class Create_employee_request(BaseModel):
    staff: str = Field(... ,description="Employee staff", min_length=3, max_length=50)
    role: str = Field(... ,description="Employee role", min_length=3, max_length=50)
    schedule: str = Field(... ,description="Employee schedule", min_length=3, max_length=50)