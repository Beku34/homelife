from rest_framework_nested import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'list', views.ProductViewSet, basename='product')


product_router = routers.NestedDefaultRouter(router, r'list', lookup='product')
product_router.register(r'ratings', views.RatingViewSet, basename='product-ratings')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
]
