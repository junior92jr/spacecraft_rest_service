from django.core.management.base import BaseCommand, CommandError

from events.utils.event_utils import calculate_coordinates


class Command(BaseCommand):
    """class that create a django admin command."""

    def handle(self, *args, **options) -> None:
        """Set coordinates to Events from latitude and longitude."""

        try:
            calculate_coordinates()
            self.stdout.write(
                self.style.SUCCESS("'Event(s)' updated with coordinates."))
        except Exception as error:
            raise CommandError(f'An error occurred when updating: {error}')
