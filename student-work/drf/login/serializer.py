from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор Пользователя для преобразования из json в объет python"""
    class Meta:
        model = User
        fields = "__all__"
