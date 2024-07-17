from typing import Annotated
from database.models import Shop, User
from fastapi import APIRouter, Depends, Header
from database.base import get_session
from serializer import PydanticShop
from utils import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.put("/shop/")
async def create_shop(
        user: Annotated[User, Depends(get_current_user)],
        data: PydanticShop,
        session: AsyncSession = Depends(get_session),
    ):
    """Хэндлер создания магазина

    Args:
        user (Annotated[User, Depends): Объект пользователя
        data (PydanticShop): Данные клиента
        session (AsyncSession, optional): Defaults to Depends(get_session).

    """
    shop = Shop()
    shop.name = data.name
    # shop.owner_id = user.id
    session.add(shop)
    await session.commit()
    await session.refresh(shop)
    user.shop = shop.id
    await session.commit()
    return shop.id
