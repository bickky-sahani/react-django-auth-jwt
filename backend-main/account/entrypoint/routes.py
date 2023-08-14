from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .route_handlers import UserAccountViewSet

router = DefaultRouter()
router.register(r"user", UserAccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
