from pydantic import BaseModel, Field
from typing import Optional

class Create_animal_request(BaseModel):
    species: str = Field(... ,description="Animal species", min_length=3, max_length=50)
    age: Optional[int] = Field(None, description="Animal age")
    gender: str = Field(... ,description="Animal gender", min_length=3, max_length=50)