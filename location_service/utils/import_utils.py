import logging
from datetime import datetime

from django.db import DatabaseError, OperationalError
from django.utils.timezone import make_aware

from location_service.models import Event, Latitude, Longitude
from location_service.serializers import (
    LatitudeSerializer,
    LongitudeSerializer,
    EventSerializer,
)


logger = logging.getLogger(__name__)

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'


def import_events_data(events_dataset: dict) -> None:
    """Function that imports event items to the database."""

    events_bulk_list = []

    try:
        for event in events_dataset:
            if not Event.objects.filter(
                    event_identifier=event.get(
                            'id', 'event_identifier')).exists():
                if 'id' in event:
                    event['event_identifier'] = event.pop('id')

                EventSerializer(data=event).is_valid(raise_exception=True)
                event_instance = Event(**event)
                event_instance.occurrence_time = make_aware(
                    datetime.strptime(event['occurrence_time'], DATE_FORMAT))
                events_bulk_list.append(event_instance)

        Event.objects.bulk_create(events_bulk_list)
    except (DatabaseError, OperationalError) as error:
        logger.error(f'Database Error with: {error}')
        raise error


def import_latitudes_data(latitudes_dataset: dict) -> None:
    """Function that imports event items to the database."""

    latitudes_bulk_list = []

    for latitude in latitudes_dataset:
        LatitudeSerializer(data=latitude).is_valid(raise_exception=True)
        latitude_instance = Latitude(**latitude)
        latitude_instance.timestamp = make_aware(
                datetime.strptime(latitude['timestamp'], DATE_FORMAT))

        latitudes_bulk_list.append(latitude_instance)

    try:
        Latitude.objects.bulk_create(latitudes_bulk_list)
    except (DatabaseError, OperationalError) as error:
        logger.error(f'Unexpected Error with: {error}')
        raise error


def import_longitudes_data(longitudes_dataset: dict) -> None:
    """Function that imports event items to the database."""

    longitudes_bulk_list = []

    for longitude in longitudes_dataset:
        LongitudeSerializer(data=longitude).is_valid(raise_exception=True)
        longitude_instance = Longitude(**longitude)
        longitude_instance.timestamp = make_aware(
                datetime.strptime(longitude['timestamp'], DATE_FORMAT))
        longitudes_bulk_list.append(longitude_instance)

    try:
        Longitude.objects.bulk_create(longitudes_bulk_list)
    except (DatabaseError, OperationalError) as error:
        logger.error(f'Unexpected Error with: {error}')
        raise error
