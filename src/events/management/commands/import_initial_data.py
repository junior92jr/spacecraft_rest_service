import json

from django.core.management.base import BaseCommand, CommandError

from events.utils.import_utils import (
    import_events_data,
    import_latitudes_data,
    import_longitudes_data
)


class Command(BaseCommand):
    """class that create a django admin command."""

    def import_events(self) -> None:
        """Handler for importing event items to the database."""

        try:
            import_events_data(
                self.load_json_file('resources/initial_data/events.json'))

            self.stdout.write(self.style.SUCCESS("'Event(s)' inserted."))

        except Exception as error:
            raise CommandError(
                f'An error occurred when inserting data: {error}')

    def import_latitudes(self) -> None:
        """Handler for importing latitudes items to the database."""

        try:
            import_latitudes_data(
                self.load_json_file('resources/initial_data/latitudes.json'))

            self.stdout.write(self.style.SUCCESS("'Latitude(s)' inserted."))

        except Exception as error:
            raise CommandError(
                f'An error occurred when inserting data: {error}')

    def import_longitudes(self) -> None:
        """Handler for importing longitudes items to the database."""

        try:
            import_longitudes_data(
                self.load_json_file('resources/initial_data/longitudes.json'))

            self.stdout.write(self.style.SUCCESS("'Longitude(s)' inserted."))

        except Exception as error:
            raise CommandError(
                f'An error occurred when inserting data: {error}')

    def load_json_file(self, file_name: str) -> dict:
        """Function that reads a json file and return a dictionary."""

        try:
            file_data = json.load(open(file_name))

            return file_data
        except OSError:
            raise CommandError(f'File {file_name} does not exist')
        except Exception as error:
            raise CommandError(f'An error occurred when reading data: {error}')

    def handle(self, *args, **options) -> None:
        """Reads the files from resources foler and populate the database."""

        self.import_events()
        self.import_latitudes()
        self.import_longitudes()
