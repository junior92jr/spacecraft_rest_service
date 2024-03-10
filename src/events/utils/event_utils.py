import logging

from django.db import DatabaseError, OperationalError

from events.models import Event, Latitude, Longitude


logger = logging.getLogger(__name__)


def calculate_coordinates() -> None:
    """Function that calculates the nearest coordinates based on an event."""

    try:
        for event in Event.objects.all():
            event_latitude = Latitude.objects.get_closest_to_target_date(
                event.occurrence_time)

            event_longitude = Longitude.objects.get_closest_to_target_date(
                event.occurrence_time)

            event.latitude = event_latitude.position
            event.longitude = event_longitude.position
            event.save()
    except (DatabaseError, OperationalError) as error:
        logger.error(f'Database Error with: {error}')
        raise error
