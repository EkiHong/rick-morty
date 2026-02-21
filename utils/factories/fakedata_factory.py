from polyfactory.factories.pydantic_factory import ModelFactory
from schemas.json_placeholder import JsonPlaceholderRequestModel
# from schemas.location import LocationResponseModel


class JsonPlaceholderFactory(ModelFactory[JsonPlaceholderRequestModel]):
    __model__ = JsonPlaceholderRequestModel
    

# class LocationFactory(ModelFactory[LocationResponseModel]):
#     __model__ = LocationResponseModel
