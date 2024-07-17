from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Product, Shop


class ProductSerialize(serializers.ModelSerializer):
    """Сериализатор товаров для преобразования из json в объет python"""
    
    class Meta:
        model = Product
        fields = ['articule', 'name', 'description', 'photo', 'price', 'shop']
        many = True


class ShopSerialize(serializers.ModelSerializer):
    """Сериализатор магазина для преобразования из json в объет python"""
    
    class Meta:
        model = Shop
        fields = ['name', 'owner']
        many = True
        