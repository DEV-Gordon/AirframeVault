from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    ManufacturerViewSet,
    DeveloperViewSet,
    RoleViewSet,
    AircraftTypeViewSet,
    AircraftImageViewSet,
    AircraftVideoViewSet,
)

router = DefaultRouter()
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"developers", DeveloperViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"aircraft-types", AircraftTypeViewSet)
router.register(r"aircraft-images", AircraftImageViewSet)
router.register(r"aircraft-videos", AircraftVideoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
