
from typing import Annotated
from fastapi import Depends, HTTPException, Header, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_session
from database.models import Token, User


async def decode_token(Authorization: str, sesion: AsyncSession) -> User:
    """функция преобразующая Authorization header в пользователя из БД

    Args:
        Authorization (str):
        sesion (AsyncSession): 

    Returns:
        User: Пользователь БД
    """
    q = await sesion.execute(select(Token).where(Token.token == Authorization))
    token_obj = q.scalar_one_or_none()
    if token_obj:
        user = await sesion.get(User, token_obj.user)
        return user


async def get_current_user(
                            Authorization: Annotated[str, Header()],
                            session: AsyncSession = Depends(get_session)
                           ) -> User:
    """Функция определяющая авторизован пользователь или нет.
    Если нет HTTPException

    Args:
        Authorization (Annotated[str, Header): 
        session (AsyncSession, optional): Defaults to Depends(get_session).

    Raises:
        HTTPException: HTTP_401_UNAUTHORIZED

    Returns:
        User
    """
    user = await decode_token(Authorization, session)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
