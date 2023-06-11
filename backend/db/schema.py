from pydantic import BaseModel
from typing import Optional
from bson.objectid import ObjectId
import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


class User(BaseModel):
    nickname: str
    password: str


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    nickname: Optional[str] = None


class Predict(BaseModel):
    stock: str
    days: int
