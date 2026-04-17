"""
API viewsets for AirframeVault.
All viewsets are read-only: only GET/HEAD/OPTIONS are allowed.
Admin panel is required for create/update/delete.
"""
from rest_framework import viewsets, mixins
from apps.core.models import (
	ManuFacturer,
	Developer,
	Role,
	AircraftType,
	AircraftImage,
	AircraftVideo,
)
from .serializers import (
	ManufacturerSerializer,
	DeveloperSerializer,
	RoleSerializer,
	AircraftTypeSerializer,
	AircraftImageSerializer,
	AircraftVideoSerializer,
)


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
	"""Read-only API endpoint for manufacturers. Filterable by name."""
	queryset = ManuFacturer.objects.all()
	serializer_class = ManufacturerSerializer
	filterset_fields = ("name",)


class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
	"""Read-only API endpoint for developers. Filterable by name."""
	queryset = Developer.objects.all()
	serializer_class = DeveloperSerializer
	filterset_fields = ("name",)


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
	"""Read-only API endpoint for roles. Filterable by code and name."""
	queryset = Role.objects.all()
	serializer_class = RoleSerializer
	filterset_fields = ("code", "name")


class AircraftTypeViewSet(viewsets.ReadOnlyModelViewSet):
	"""Read-only API endpoint for aircraft types. Filterable by country, era, manufacturer, fidelity_level, is_flayable, roles."""
	queryset = AircraftType.objects.all()
	serializer_class = AircraftTypeSerializer
	filterset_fields = ("country", "era", "manufacturer", "fidelity_level", "is_flayable", "roles")


class AircraftImageViewSet(viewsets.ReadOnlyModelViewSet):
	"""Read-only API endpoint for aircraft images. Filterable by aircraft."""
	queryset = AircraftImage.objects.all()
	serializer_class = AircraftImageSerializer
	filterset_fields = ("aircraft",)


class AircraftVideoViewSet(viewsets.ReadOnlyModelViewSet):
	"""Read-only API endpoint for aircraft videos. Filterable by aircraft and provider."""
	queryset = AircraftVideo.objects.all()
	serializer_class = AircraftVideoSerializer
	filterset_fields = ("aircraft", "provider")