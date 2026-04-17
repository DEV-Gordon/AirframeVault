"""
Serializers for AirframeVault API.
Expose all fields for each model, including nested images/videos for AircraftType.
"""

from rest_framework import serializers
from apps.core.models import (
    ManuFacturer,
    Developer,
    Role,
    AircraftType,
    AircraftImage,
    AircraftVideo,
)


class ManufacturerSerializer(serializers.ModelSerializer):
    """Serializer for manufacturer model."""
    class Meta:
        model = ManuFacturer
        fields = "__all__"


class DeveloperSerializer(serializers.ModelSerializer):
    """Serializer for developer model."""
    class Meta:
        model = Developer
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    """Serializer for role model."""
    class Meta:
        model = Role
        fields = "__all__"


class AircraftImageSerializer(serializers.ModelSerializer):
    """Serializer for aircraft image model."""
    class Meta:
        model = AircraftImage
        fields = "__all__"


class AircraftVideoSerializer(serializers.ModelSerializer):
    """Serializer for aircraft video model."""
    class Meta:
        model = AircraftVideo
        fields = "__all__"


class AircraftTypeSerializer(serializers.ModelSerializer):
    """Serializer for aircraft type model, includes nested images and videos."""
    images = AircraftImageSerializer(many=True, read_only=True)
    videos = AircraftVideoSerializer(many=True, read_only=True)

    class Meta:
        model = AircraftType
        fields = "__all__"
