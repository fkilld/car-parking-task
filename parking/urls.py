from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarParkingDetailsViewSet

router = DefaultRouter()
router.register('carparkingdetails', CarParkingDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
