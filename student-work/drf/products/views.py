from loguru import logger
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from products.serializers import ProductSerialize, ShopSerialize
from .models import Product, Shop
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """view отвечающая за управление товарами"""

    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerialize
    permission_classes = [permissions.IsAuthenticated]


    def retrieve(self, request, *args, **kwargs):
        """Метод получения конкретного товара из бд"""
        articule = kwargs['pk']
        logger.debug(articule)
        
        product = Product.objects.filter(articule=articule).first()
        if product:
            serializer = ProductSerialize(product)
            return Response(serializer.data)
        else:
            return Response({"message": "Not found"})

    def create(self, request, *args, **kwargs):
        """Метод создания объекта/объектов товара из бд"""
        data = request.data

        serialized_data = self.get_serializer(data=data, many=True)
        serialized_data.is_valid(raise_exception=True)

        self.perform_create(serialized_data)

        return Response({"message": "Objects created successfully"}, status=201)

    def destroy(self, request, *args, **kwargs):
        """Метод удаления товара из бд"""
        articule = kwargs['pk']  # получаем артикул товара из URL параметра   
        product = Product.objects.filter(articule=articule)
        if product.exists():
            product.delete()
            return Response({"message": "Товар успешно удален"}, status=204)
        return Response({"message": "Товар с таким артикулом не найден"}, status=404)

    def partial_update(self, request, *args, **kwargs):
        """Метод частичного обновления товара в бд"""
        articule = kwargs['pk']
        
        product = Product.objects.filter(articule=articule)
        if product.exists():
            serialized_data = self.get_serializer(product.first(), data=request.data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                return  Response(serialized_data.data)
            else:
                return  Response(serialized_data.errors)

    @action(detail=False, methods=['delete']) 
    def multiple_delete(self, request, *args, **kwargs):
        """Метод множественного удаления товаров из бд"""
        data = request.data

        if len(data) == 0:
            return Response({'error': 'Передайте артикулы товаров'}, status=400)

        try:
            for articule in data:
                Product.objects.filter(articule__in=articule).delete()
            return Response({'message': 'Товар успешно удален'}, status=204)
        except:
            return Response({'error': 'Ошибка при удалении товара'}, status=500)


    def perform_create(self, serializer):
        """"Метод непосредственного сохранения товаров в бд"""
        serializer.save()
        
    def perform_destroy(self, instance):
        """"Метод непосредственного сохранения товаров в бд"""
        instance.delete()


class ShopViewSet(viewsets.ModelViewSet):
    """view отвечающая за управление магазинам"""
    queryset = Shop.objects.all().order_by('name')
    serializer_class = ShopSerialize
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        """Метод создания объекта/объектов магазина из бд"""
        data = request.data
        data["owner"] = request.user.id        
        serialized_data = self.get_serializer(data=data)
        serialized_data.is_valid(raise_exception=True)

        self.perform_create(serialized_data)
        
        return Response({"message": "Магазин успешно создан"}, status=201)

    def perform_create(self, serializer):
        """"Метод непосредственного сохранения объекта магазина в бд"""
        serializer.save()
