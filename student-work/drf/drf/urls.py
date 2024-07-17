from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from login.views import UserViewSet
from products.views import ProductViewSet, ShopViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'shops', ShopViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('products/<str:article>/', ProductViewSet.as_view({'delete': 'destroy'})),
    path('token/', obtain_auth_token),
]