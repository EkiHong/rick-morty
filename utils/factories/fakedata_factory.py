from polyfactory.factories.pydantic_factory import ModelFactory
from schemas.json_placeholder import JsonPlaceholderRequestModel
from schemas.location import LocationQueryParamsRequestModel


class LocationFactory(ModelFactory[LocationQueryParamsRequestModel]):
    __model__ = LocationQueryParamsRequestModel


class JsonPlaceholderFactory(ModelFactory[JsonPlaceholderRequestModel]):
    __model__ = JsonPlaceholderRequestModel
