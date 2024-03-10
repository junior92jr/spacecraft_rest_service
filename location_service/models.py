from django.db import models


class CustomDateQuerySet(models.QuerySet):
    """Queryset class that enables date operations."""

    def get_closest_to_target_date(self, target_date):
        """Retrieves the position with the closest target date."""

        greater_date = self.filter(
            timestamp__gte=target_date).order_by("timestamp").first()
        less_date = self.filter(
            timestamp__lte=target_date).order_by("-timestamp").first()

        if greater_date and less_date:
            return greater_date if abs(
                greater_date.timestamp - target_date) < abs(
                    less_date.timestamp - target_date) else less_date
        else:
            return greater_date or less_date


class Event(models.Model):
    """Model that represents events in the database."""

    event_identifier = models.CharField(max_length=10)
    event_name = models.CharField(max_length=60)
    severity = models.CharField(max_length=10)
    occurrence_time = models.DateTimeField()
    latitude = models.DecimalField(max_digits=6, decimal_places=4, null=True)
    longitude = models.DecimalField(max_digits=7, decimal_places=4, null=True)

    def __str__(self) -> str:
        return self.event_identifier


class Latitude(models.Model):
    """Model that represents latitudes in the database."""

    timestamp = models.DateTimeField()
    position = models.DecimalField(max_digits=6, decimal_places=4)

    objects = CustomDateQuerySet.as_manager()


class Longitude(models.Model):
    """Model that represents longitudes in the database."""

    timestamp = models.DateTimeField()
    position = models.DecimalField(max_digits=7, decimal_places=4)

    objects = CustomDateQuerySet.as_manager()
