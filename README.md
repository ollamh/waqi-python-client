# WAQI Python Client

Python client library for the World Air Quality Index (WAQI) APIs. See documentation [here](https://aqicn.org/json-api/doc/).
All available API modules are supported - City feed, Geolocalized feed, Search, and Map Queries.

### Installation

The project is managed using Hatch ([documentation](https://hatch.pypa.io/latest/install/)). After Hatch is installed, proceed with commands   

```bash

hatch env create  # Creates virtual environment
hatch shell  # Enable virtual environment 
hatch build .  # Builds the package wheel and sdist artifacts
```

It will provide the sdist and wheel artifacts that later can be installed via `pip`.

### Get API key

Sign up for an API key [here](https://aqicn.org/data-platform/token/)

### Making Requests

The primary `WaqiAPI` class in the `waqi_api` module is a factory class that creates objects for each of the API modules, allowing you to make requests to any of them with your desired request parameters. You have to first create an object for it, then access your desired API module via the object. See the code snippets below:

```python

WAQI_TOKEN = 'Obtained API key'

from waqi_python_client.waqi_api import WaqiAPI

api = WaqiAPI(WAQI_TOKEN)
```

**For City Feed:**

```py
response = api.city_feed().set_city("Munich").fetch()
```

**For Search:**

```py
response = api.search().set_keyword("Johannesburg").fetch()
```

**For Lat/Lng based Geolocalized feed:**

```py
response = api.geo_feed().set_coordinates(37.7749, -122.4194).fetch()
```

**For IP based Geolocalized feed:**

```py
response = api.ip_feed().set_ip("MY_IP").fetch()
```

**For Map Queries:**

```py
response = api.map_station().set_map_bounds(40.712, -74.006, 34.052, -118.243).fetch()
```

## Tests

```bash
hatch shell
hatch test
```