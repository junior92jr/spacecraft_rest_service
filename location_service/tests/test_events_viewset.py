from rest_framework.test import APITestCase
from rest_framework import status

from location_service.utils.import_utils import (
    import_events_data,
    import_latitudes_data,
    import_longitudes_data,
)
from location_service.utils.event_utils import calculate_coordinates

from .resources import (
    TEST_EVENTS_OK,
    TEST_LATITUDES_OK,
    TEST_LONGITUDES_OK,
)


class EventsViewSetTestCase(APITestCase):
    """Test case that handles unit testing for Events."""

    def setUp(self) -> None:
        """Setup method for Unit tests."""

        import_events_data(TEST_EVENTS_OK)
        import_latitudes_data(TEST_LATITUDES_OK)
        import_longitudes_data(TEST_LONGITUDES_OK)

        calculate_coordinates()

    def test_get_event_list_200(self) -> None:
        """Check success response from events api."""

        response = self.client.get('/api/v1/events/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json_response = response.json()

        self.assertEqual(
            type(json_response.get('results')), list)
        self.assertEqual(
            len(json_response.get('results')), 3)
        self.assertEqual(
            json_response.get('count'), 3)
        self.assertEqual(
            json_response.get('next'), None)
        self.assertEqual(
            json_response.get('previous'), None)

    def test_get_event_by_id_200(self) -> None:
        """Check success response from events api."""

        response = self.client.get('/api/v1/events/E001/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json_response = response.json()

        self.assertEqual(
            type(json_response), dict)
        self.assertEqual(
            json_response.get('event_identifier'), "E001")
        self.assertEqual(
            json_response.get('event_name'), "System Startup")
        self.assertEqual(
            json_response.get('severity'), "Info")
        self.assertEqual(
            json_response.get('occurrence_time'), "2023-10-01T10:15:00Z")
        self.assertEqual(
            json_response.get('latitude'), "35.1234")
        self.assertEqual(
            json_response.get('longitude'), "-117.2437")

        response = self.client.get('/api/v1/events/E002/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json_response = response.json()

        self.assertEqual(
            type(json_response), dict)
        self.assertEqual(
            json_response.get('event_identifier'), "E002")
        self.assertEqual(
            json_response.get('event_name'), "Navigation Calibration")
        self.assertEqual(
            json_response.get('severity'), "Info")
        self.assertEqual(
            json_response.get('occurrence_time'), "2023-10-01T10:35:00Z")
        self.assertEqual(
            json_response.get('latitude'), "37.3245")
        self.assertEqual(
            json_response.get('longitude'), "-115.2437")

        response = self.client.get('/api/v1/events/E003/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json_response = response.json()

        self.assertEqual(
            type(json_response), dict)
        self.assertEqual(
            json_response.get('event_identifier'), "E003")
        self.assertEqual(
            json_response.get('event_name'), "Warning Light On")
        self.assertEqual(
            json_response.get('severity'), "Warning")
        self.assertEqual(
            json_response.get('occurrence_time'), "2023-10-01T10:50:00Z")
        self.assertEqual(
            json_response.get('latitude'), "39.5567")
        self.assertEqual(
            json_response.get('longitude'), "-113.2437")

    def test_get_event_by_id_404(self) -> None:
        """Check not found response from events api."""

        response = self.client.get('/api/v1/events/dasdas/', format='json')
        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND)

        json_response = response.json()

        self.assertEqual(
            json_response.get('detail'), "Not found.")
