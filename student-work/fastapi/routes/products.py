from typing import Annotated, List, Union

from sqlalchemy import select
from fastapi import APIRouter, Depends
from database.base import get_session
from database.models import Product, User
from serializer import PydanticProduct, PydanticProductUpdate, PydanticProductsArray
from utils import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger


router = APIRouter()

@router.post("/products/")
async def add_products(
        user: Annotated[User, Depends(get_current_user)],
        data: Union[PydanticProduct, PydanticProductsArray],
        session: AsyncSession = Depends(get_session),
    ):
    """Хэндлер добавляет один/список товаров в БД

    Args:
        user (Annotated[User, Depends): Объект пользователя
        data (Union[PydanticProduct, PydanticProductsArray]): Данные от клинета
        session (AsyncSession, optional): Defaults to Depends(get_session).

    """
    if user.shop is None:
        return {"message": "shop not found"}
    if isinstance(data, PydanticProductsArray):
        products = []
        for product_data in data.prodcuts:
            product = Product()
            product.articule = product_data.articule
            product.description = product_data.description
            product.name = product_data.name
            product.price = product_data.price
            product.photo = product_data.photo
            product.shop = user.shop
            products.append(product)
        
        session.add_all(products)
        await session.commit()
        
        return 1
    else:
        product = Product()
        product.articule = data.articule
        product.description = data.description
        product.name = data.name
        product.price = data.price
        product.photo = data.photo
        product.shop = user.shop

        session.add(product)
        await session.commit()
        
        return 1


@router.get("/products/")
async def get_products_list(
        user: Annotated[str, Depends(get_current_user)],
        session: AsyncSession = Depends(get_session),
    ):
    """Хэндлер для получения всех объектов

    Args:
        user (Annotated[str, Depends): Объект пользователя
        session (AsyncSession, optional): Defaults to Depends(get_session).

    """
    q = await session.execute(select(Product))
    products_list = q.scalars()

    products = []
    
    for product in products_list:
        products.append({
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "photo": product.photo,
            "articule": product.articule,
            "shop": product.shop
        })
    
    return {"products": products}

@router.get("/products/{articule}")
async def get_product(
        articule: str,
        user: Annotated[str, Depends(get_current_user)],
        session: AsyncSession = Depends(get_session),
    ):
    """Хэндлер детального обзора товара по артикулу

    Args:
        articule (str): артикул товара
        user (Annotated[str, Depends): Объект пользователя
        session (AsyncSession, optional): Defaults to Depends(get_session).

    """
    q = await session.execute(select(Product).where(Product.articule==articule))
    product = q.scalar_one_or_none()
    if product:
        return {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "photo": product.photo,
            "articule": product.articule,
            "shop": product.shop
        }
    else:
        return None


@router.patch("/products/{articule}")
async def get_products_list(
        articule: str,
        data: PydanticProductUpdate,
        user: Annotated[str, Depends(get_current_user)],
        session: AsyncSession = Depends(get_session),
    ):
    """Хэндлер обновления товара по артикулу

    Args:
        articule (str): Артикул
        data (PydanticProductUpdate): Данные клиента
        user (Annotated[str, Depends): Объект пользователя
        session (AsyncSession, optional):. Defaults to Depends(get_session).

    """
    q = await session.execute(select(Product).where(Product.articule==articule))
    product = q.scalar_one_or_none()
    if product:
        if data.articule:
            product.articule = data.articule
        if data.description:
            product.description = data.description
        if data.price:
            product.price = data.price
        if data.photo:
            product.photo = data.photo
        if data.name:
            product.name = data.name
            
        await session.commit()
        
        return {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "photo": product.photo,
            "articule": product.articule,
            "shop": product.shop
        }


@router.delete("/products/{articule}")
async def delete_product(
    articule: str,
    user: Annotated[str, Depends(get_current_user)],
    session: AsyncSession = Depends(get_session),
):
    """Хэндлер удаления товара по артикулу

    Args:
        articule (str): Артикул
        user (Annotated[str, Depends): Объект пользователя
        session (AsyncSession, optional):. Defaults to Depends(get_session).

    """
    q = await session.execute(select(Product).where(Product.articule==articule))
    product = q.scalar_one_or_none()
    if product:
        await session.delete(product)
        await session.commit()
        return 1
    return 0


@router.delete("/products/")
async def delete_products(
    articules: List[str],
    user: Annotated[str, Depends(get_current_user)],
    session: AsyncSession = Depends(get_session),
):
    """Хэндлер множесвтенного удаления товаров

    Args:
        articules (List[str]): Список с артикулами
        user (Annotated[str, Depends): Объект пользователя
        session (AsyncSession, optional): Defaults to Depends(get_session).
    """
    for articule in articules:
        q = await session.execute(select(Product).where(Product.articule==articule))
        product = q.scalar_one_or_none()
        if product:
            await session.delete(product)
    await session.commit()

    return 1