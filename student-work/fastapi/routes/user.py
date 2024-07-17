import secrets
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_session
from database.models import Token, User
from utils import get_current_user
from serializer import PydanticUser
from loguru import logger

router = APIRouter()


@router.post("/auth/token")
async def login_for_access_token(
    form_data: PydanticUser,
    session: AsyncSession = Depends(get_session),
    ):
    """Эндпоинт для получения токена

    Args:
        form_data (PydanticUser)
        request (Request): 
        session (AsyncSession, optional): Defaults to Depends(get_session).
    """
    q = await session.execute(select(User).where(User.username==form_data.username))
    user = q.scalar_one_or_none()
    if user:
        q = await session.execute(select(Token).where(Token.user==user.id))
        token = q.scalar_one_or_none()
        if user.password == form_data.password:
            if token:
                return token.token

            token = secrets.token_urlsafe(16)
            token_object = Token()
            token_object.token = token
            token_object.user = user.id
            session.add(token_object)
            await session.commit()
            return token
        return {"error": "password incorrect"}
    else:
        return {"error": "username incorrect"}


@router.post("/register")
async def register(
    data: PydanticUser,
    session: AsyncSession = Depends(get_session)
    ):
    q = await session.execute(select(User).where(User.username==data.username))
    user = q.scalar_one_or_none()
    if user:
        return {"message":"already registred"}
    user = User()
    user.password = data.password
    user.username = data.username
    session.add(user)
    await session.commit()
    return {
        "username": data.username,
        "password": data.password
    }
    
@router.post("/auth/token")
async def login_for_access_token(
    form_data: PydanticUser,
    session: AsyncSession = Depends(get_session),
    ):
    """Эндпоинт для получения токена

    Args:
        form_data (PydanticUser)
        request (Request): 
        session (AsyncSession, optional): Defaults to Depends(get_session).
    """
    q = await session.execute(select(User).where(User.username==form_data.username))
    user = q.scalar_one_or_none()
    if user:
        q = await session.execute(select(Token).where(Token.user==user.id))
        token = q.scalar_one_or_none()
        if user.password == form_data.password:
            if token:
                return token.token

            token = secrets.token_urlsafe(16)
            token_object = Token()
            token_object.token = token
            token_object.user = user.id
            session.add(token_object)
            await session.commit()
            return token
        return {"error": "password or username incorrect"}
    else:
        return {"error": "password or username incorrect"}


@router.patch("/auth/token")
async def update_token(
        user: Annotated[str, Depends(get_current_user)],
        Authorization: Annotated[str, Header()],
        session: AsyncSession = Depends(get_session),
    ):
    """Хэндлер перевыпуска токена

    Args:
        user (Annotated[str, Depends): Объект пользователя
        Authorization (Annotated[str, Header): Хедер авторизации
        session (AsyncSession, optional): Defaults to Depends(get_session).

    Returns:
        _type_: _description_
    """
    q = await session.execute(select(Token).where(Token.token==Authorization))
    token = q.scalar_one_or_none()
    if token:
        await session.delete(token)
    token = Token()
    token.token = secrets.token_urlsafe(16)
    token.user = user.id
    
    session.add(token)
    await session.commit()
    
    return {"token": token.token}