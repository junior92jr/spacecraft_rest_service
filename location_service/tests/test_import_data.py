from django.test import TestCase
from rest_framework.exceptions import ValidationError

from location_service.models import Event, Latitude, Longitude
from location_service.utils.import_utils import (
    import_events_data,
    import_latitudes_data,
    import_longitudes_data,
)

from .resources import (
    TEST_EVENTS_OK,
    TEST_LATITUDES_OK,
    TEST_LONGITUDES_OK,
    TEST_EVENTS_INVALID_DATETIME,
    TEST_LATITUDES_INVALID_DATETIME,
    TEST_LONGITUDES_INVALID_DATETIME,
    TEST_LATITUDES_INVALID_POSITION,
    TEST_LONGITUDES_INVALID_POSITION
)


class ImportTestCase(TestCase):
    """Test case that handles unit testing for Events."""

    def test_events_imported_data(self) -> None:
        """Check Events imported in the database."""

        import_events_data(TEST_EVENTS_OK)

        inserted_events = Event.objects.all()

        event_1 = Event.objects.get(event_identifier="E001")
        event_2 = Event.objects.get(event_identifier="E002")
        event_3 = Event.objects.get(event_identifier="E003")

        self.assertEqual(inserted_events.count(), 3)

        self.assertEqual(event_1.event_identifier, "E001")
        self.assertEqual(event_1.event_name, "System Startup")
        self.assertEqual(event_1.severity, "Info")

        self.assertEqual(event_2.event_identifier, "E002")
        self.assertEqual(event_2.event_name, "Navigation Calibration")
        self.assertEqual(event_2.severity, "Info")

        self.assertEqual(event_3.event_identifier, "E003")
        self.assertEqual(event_3.event_name, "Warning Light On")
        self.assertEqual(event_3.severity, "Warning")

    def test_events_invalid_datetime(self) -> None:
        """Check Events imported in the database with invalid Datetime."""

        with self.assertRaises(ValidationError) as catched_exception:
            import_events_data(TEST_EVENTS_INVALID_DATETIME)

        self.assertEqual(ValidationError, type(catched_exception.exception))

    def test_coordinates_data(self) -> None:
        """Check Coordinates imported in the database."""

        import_latitudes_data(TEST_LATITUDES_OK)
        import_longitudes_data(TEST_LONGITUDES_OK)

        inserted_latitudes = Latitude.objects.all()
        inserted_longitudes = Longitude.objects.all()

        self.assertEqual(inserted_latitudes.count(), 6)
        self.assertEqual(inserted_longitudes.count(), 6)

    def test_coordinates_invalid_datetime(self) -> None:
        """Check Coordinates imported in the database with invalid Datetime."""

        with self.assertRaises(ValidationError) as catched_exception:
            import_latitudes_data(TEST_LATITUDES_INVALID_DATETIME)

        self.assertEqual(ValidationError, type(catched_exception.exception))

        with self.assertRaises(ValidationError) as catched_exception:
            import_latitudes_data(TEST_LATITUDES_INVALID_POSITION)

        self.assertEqual(ValidationError, type(catched_exception.exception))

        with self.assertRaises(ValidationError) as catched_exception:
            import_longitudes_data(TEST_LONGITUDES_INVALID_DATETIME)

        self.assertEqual(ValidationError, type(catched_exception.exception))

        with self.assertRaises(ValidationError) as catched_exception:
            import_longitudes_data(TEST_LONGITUDES_INVALID_POSITION)

        self.assertEqual(ValidationError, type(catched_exception.exception))
