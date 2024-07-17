from loguru import logger
from rest_framework import authentication, permissions
from rest_framework import permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from login.serializer import UserSerializer
from rest_framework.decorators import action



class UserViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для управления пользователями
    """
    def get_permissions(self):
    # Your logic should be all here
        logger.debug(self.action)
        
        if self.action == 'register':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated ]

        return super(UserViewSet, self).get_permissions()
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False, methods=['post']) 
    def change_token(self, request, *args, **kwargs):
        """
        Метод смены API токена
        """
        user = request.user
        Token.objects.get(user=User.objects.get(id=user.id)).delete()
        
        token = Token.objects.create(user=user)
        
        return Response({"token": str(token)})


    @action(detail=False, methods=['post']) 
    def register(self, request, *args, **kwargs):
        """Вью для регистрации"""
        data = request.data
    
        user = User.objects.create_user(data["username"], password=data["password"])
        token = Token.objects.get_or_create(user=user)

        return Response(token[0].key, status=200)