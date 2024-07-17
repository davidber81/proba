from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from loguru import logger
# Create your models here.


class Shop(models.Model):
    """Модель отвечающая за данные о магазине
    
    Поля:
        name (CharField): Наименование магазина
        owner (ForeignKey): Владелец магазина
    """
    name = models.CharField(max_length=70)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Product(models.Model):
    """Модель отвечающая за данные о товарах

    Поля:
        name (CharField): Наименование товара максимум 70 символов
        description (TextField): Описание товара
        photo (ImageField): Путь к изображению товара в папке images
        price (FloatField): Цена товара
        articule (CharField): Уникальный артикул товара
        shop (ForeignKey): Ссылка на магазин
    """
    name = models.CharField(max_length=70)
    description = models.TextField()
    photo = models.ImageField(upload_to="images", null=True)
    price = models.FloatField(default=False)
    articule = models.CharField(max_length=70, unique=True)
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)

