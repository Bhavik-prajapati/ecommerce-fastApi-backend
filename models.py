from typing import List
from pydantic import BaseModel

class Review(BaseModel):
    text: str

class ReviewList(BaseModel):
    reviews: List[str]
