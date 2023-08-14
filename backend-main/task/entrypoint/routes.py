from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .route_handlers import TaskViewSet

router = DefaultRouter()
router.register(r"", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
