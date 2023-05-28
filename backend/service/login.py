from fastapi import HTTPException, status
from utils.auth import Hash
from utils.jwt import create_access_token
from db.database import db


def login(request):
    user = db["users"].find_one({"nickname": request.nickname})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="닉네임 혹은 비밀번호 정보가 일치하지 않습니다.",
        )
    if not Hash.verify(user["password"], request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="닉네임 혹은 비밀번호 정보가 일치하지 않습니다.",
        )

    access_token = create_access_token(data={"sub": user["nickname"]})
    return {"access_token": access_token, "nickname": user["nickname"]}
