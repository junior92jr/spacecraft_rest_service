# Spacecraft Rest Service

The project is to design and implement a Restfull API that provides the location of an event.

## API Endpoints

This API implements the following endpoints:

`GET` : `api/v1/events/` Get a list of all events with their Locations paginated by 10 items per page.

`GET` : `api/v1/events/<str>/` Retrieve a single Event with its associated location.

## API Examples

### List all events and their associated locations
```bash
curl --location 'http://localhost:8000/api/v1/events/'
```

#### Response

```bash
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "event_identifier": "E001",
            "event_name": "System Startup",
            "severity": "Info",
            "occurrence_time": "2023-10-01T10:15:00Z",
            "latitude": "35.1234",
            "longitude": "-117.2437"
        },
        {
            "event_identifier": "E002",
            "event_name": "Navigation Calibration",
            "severity": "Info",
            "occurrence_time": "2023-10-01T10:35:00Z",
            "latitude": "37.3245",
            "longitude": "-115.2437"
        },
        {
            "event_identifier": "E003",
            "event_name": "Warning Light On",
            "severity": "Warning",
            "occurrence_time": "2023-10-01T10:50:00Z",
            "latitude": "39.5567",
            "longitude": "-113.2437"
        },
        {
            "event_identifier": "E004",
            "event_name": "Data Transmission Error",
            "severity": "Error",
            "occurrence_time": "2023-10-01T11:05:00Z",
            "latitude": "40.6742",
            "longitude": "-112.2437"
        },
        {
            "event_identifier": "E005",
            "event_name": "System Restart",
            "severity": "Info",
            "occurrence_time": "2023-10-01T11:25:00Z",
            "latitude": "42.8865",
            "longitude": "-110.2437"
        },
        {
            "event_identifier": "E006",
            "event_name": "Low Battery",
            "severity": "Warning",
            "occurrence_time": "2023-10-01T11:45:00Z",
            "latitude": "45.0123",
            "longitude": "-108.2437"
        },
        {
            "event_identifier": "E007",
            "event_name": "Data Loss",
            "severity": "Error",
            "occurrence_time": "2023-10-01T12:05:00Z",
            "latitude": "47.2134",
            "longitude": "-106.2437"
        },
        {
            "event_identifier": "E008",
            "event_name": "Critical System Failure",
            "severity": "Error",
            "occurrence_time": "2023-10-01T12:20:00Z",
            "latitude": "49.4257",
            "longitude": "-104.2437"
        },
        {
            "event_identifier": "E009",
            "event_name": "System Reboot",
            "severity": "Info",
            "occurrence_time": "2023-10-01T12:45:00Z",
            "latitude": "51.6321",
            "longitude": "-102.2437"
        },
        {
            "event_identifier": "E010",
            "event_name": "Sensor Malfunction",
            "severity": "Error",
            "occurrence_time": "2023-10-07T13:00:00Z",
            "latitude": "75.4236",
            "longitude": "-80.2437"
        }
    ]
}
```

### List all events and their associated locations
```bash
curl --location 'http://localhost:8000/api/v1/events/E010'
```

#### Response
```bash
{
    "event_identifier": "E010",
    "event_name": "Sensor Malfunction",
    "severity": "Error",
    "occurrence_time": "2023-10-07T13:00:00Z",
    "latitude": "75.4236",
    "longitude": "-80.2437"
}
```

## Clone the repository

To clone the repository by SHH

```bash
$ git clone git@github.com:junior92jr/spacecraft_rest_service.git
```

To clone the repository by HTTPS

```bash
$ git clone https://github.com/junior92jr/spacecraft_rest_service.git
```

## Build the API image

To build, test and run this API we'll be using `docker-compose`. As such, the first step
is to build the images defined in the `docker-compose.yml` file.

```bash
$ cd spacecraft_rest_service/
```

```bash
$ docker-compose build
```

This will build two images:

- `django-app` image with the Django App.
- `postgres-db` image with Postgres database.

## Create Enviroment Variables

You will find a file called `.env_example`, rename it for `.env`


## Run the Containers
 
To run the containers previously built, execute the following:
 
```bash
$ docker-compose up -d
```

To make sure the app is running correctly open [http://localhost:8000](http://localhost:8000).

## Check database is running

One can confirm that the database was properly created by accessing the database container
and starting a psql console.

```bash
$ docker-compose exec web-db psql -U postgres
```

## Import Initial Data

We need to run the django commands to import the database with events and coordinates.

```bash
$ docker-compose exec web python manage.py import_initial_data
```
```bash
$ docker-compose exec web python manage.py set_coordinates
```

## Run the Tests

The tests can be executed with:

```bash
$ docker-compose exec web python manage.py test --settings=spacecraft_api.test_settings
```
