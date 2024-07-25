from django.urls import path, include
from . import views  # Импортируем представления (views) из текущего приложения

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

# Основной роутер для 'carts'
router = DefaultRouter()
router.register(r'carts', views.CartViewSet)  # Регистрируем представление CartViewSet по маршруту 'carts'

# Создаем вложенный роутер для 'items' внутри 'carts'
nested_router = NestedDefaultRouter(router, r'carts', lookup='cart')
nested_router.register(r'items', views.CartItemViewSet, basename='cart-items')

# Определяем urlpatterns для включения основных и вложенных маршрутов
urlpatterns = [
    path('', include(router.urls)),  # Включаем URL-адреса основного роутера
    path('', include(nested_router.urls)),  # Включаем URL-адреса вложенного роутера
]
