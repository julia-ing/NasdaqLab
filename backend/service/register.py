from fastapi import HTTPException, status
from utils.auth import Hash
from db.database import db


def create_user(request):
    user = db["users"].find_one({"nickname": request.nickname})
    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="닉네임 중복",
        )
    else:
        hashed_pw = Hash.encrypt(request.password)
        user_object = dict(request)
        user_object["password"] = hashed_pw
        user_id = db["users"].insert_one(user_object)
        new_user = db["users"].find_one({"_id": user_id.inserted_id})
        return new_user
