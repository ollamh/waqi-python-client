import requests
from typing import AnyStr, Any, Dict, Self, Union

BASE_URL = "https://api.waqi.info/"


class WaqiAPIEntity:
    def __init__(self, api_key: AnyStr) -> None:
        self.api_key = api_key
        self.base_url = BASE_URL
        self.query_params = {}

    def set_query_param(self, param: AnyStr, value: Any) -> Self:
        self.query_params[param] = value
        return self  # Return the class object to enable method chaining

    def set_multiple_query_params(self, **kwargs) -> Self:
        self.query_params.update(kwargs)
        return self

    def build_query_params(self) -> AnyStr:
        if not self.query_params:
            return ''
        return '&' + '&'.join([f'{param}={value}' for param, value in self.query_params.items()])

    def fetch(self, as_json=False) -> Union[AnyStr, Dict[AnyStr, Any]]:
        url = self.url() + '?token=' + self.api_key + self.build_query_params()
        response = requests.get(url)
        return response.json() if as_json else response.text

    def url(self) -> AnyStr:
        raise NotImplementedError("Subclasses must implement url()")


class CityFeed(WaqiAPIEntity):
    def set_city(self, city: AnyStr) -> Self:
        return self.set_query_param('city', city)

    def url(self) -> AnyStr:
        # /feed/:city/?token=:token
        url = f'{self.base_url}feed/{self.query_params["city"]}/'
        self.query_params = {}
        return url


class Search(WaqiAPIEntity):
    def set_keyword(self, keyword: AnyStr) -> Self:
        return self.set_query_param('keyword', keyword)

    def url(self) -> AnyStr:
        return f'{self.base_url}search/'


class GeoFeed(WaqiAPIEntity):
    def set_coordinates(self, latitude: Union[int, float], longitude: Union[int, float]) -> Self:
        return self.set_multiple_query_params(lat=latitude, lon=longitude)

    def url(self) -> AnyStr:
        # /feed/geo::lat;:lng/?token=:token
        url = f'{self.base_url}feed/geo:{self.query_params["lat"]};{self.query_params["lon"]}/'
        self.query_params = {}
        return url
    

class MapStation(WaqiAPIEntity):
    def set_map_bounds(
            self, latitude_north: Union[int, float], longitude_west: Union[int, float],
            latitude_south: Union[int, float], longitude_east: Union[int, float]):
        return self.set_query_param(
            'latlng', f"{latitude_north},{longitude_west},{latitude_south},{longitude_east}")


    def url(self) -> AnyStr:
        return f'{self.base_url}map/bounds/'
    

class IPFeed(WaqiAPIEntity):
    def set_ip(self, ip_address: AnyStr):
        return self.set_query_param('ip', ip_address)
    
    def url(self) -> AnyStr:
        return f"{self.base_url}feed/here/"
