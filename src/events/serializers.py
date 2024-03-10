from rest_framework import serializers

from .models import Event, Latitude, Longitude


class EventSerializer(serializers.ModelSerializer):
    """Model Serializer used to visualize items from Event model."""

    class Meta:
        model = Event
        fields = (
            'event_identifier',
            'event_name',
            'severity',
            'occurrence_time',
            'latitude',
            'longitude',
        )


class LatitudeSerializer(serializers.ModelSerializer):
    """Model Serializer used to visualize items from Latitude model."""

    class Meta:
        model = Latitude
        fields = (
            'timestamp',
            'position',
        )


class LongitudeSerializer(serializers.ModelSerializer):
    """Model Serializer used to visualize items from Longitude model."""

    class Meta:
        model = Longitude
        fields = (
            'timestamp',
            'position',
        )
