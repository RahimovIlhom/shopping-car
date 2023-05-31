from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, BusyCarViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'busy-cars', BusyCarViewSet, basename='busy-car')

urlpatterns = [
    path('', include(router.urls)),
]
