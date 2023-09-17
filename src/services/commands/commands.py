from flask import abort, Response
from src.services.commands.command_interface import ICommand
from enum import Enum
from src.services.rest.main_service import MainService
from http import HTTPStatus


class Commands(Enum):
    COMMAND_1 = 0,
    COMMAND_2 = 1,
    PREDICT = 2,
    DIRECT = 3,


class Command1(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command 1 executed"
        }


class Command2(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command 2 executed"
        }


class Predict(ICommand):
    def execute(self, data: dict) -> dict:
        return {
            "message": "Predict executed"
        }


class Direct(ICommand):
    def execute(self, data: dict):
        if data.get("location") is None:
            return {"Error": "location is required "}, HTTPStatus.BAD_REQUEST
        if data.get("location").get("lat") is None:
            return {"Error": "latitude (lat) is required "}, HTTPStatus.BAD_REQUEST
        if data.get("location").get("lng") is None:
            return {"Error": "longitude (lng) is required "}, HTTPStatus.BAD_REQUEST
        lat = data.get("location").get("lat")
        lng = data.get("location").get("lng")
        reference_location = {
            "type": "Point",
            "coordinates": [lat, lng]
        }
        # Use the aggregation framework to find the nearest object
        pipeline = [
            {
                "$geoNear": {
                    "near": reference_location,
                    "distanceField": "distance",
                    "spherical": True,
                    "key": "data.location.coordinates"
                }
            },
            {
                "$limit": 1  # Limit the result to one document
            }
        ]

        result = list(MainService().get_db().objects.aggregate(pipeline))
        if len(result) == 0:
            return {"Error": "No objects found"}, HTTPStatus.NOT_FOUND
        return result[0], HTTPStatus.OK



class History(ICommand):
    def execute(self) -> dict:
        return {
            "message": "History executed"
        }


class Places(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Places executed"
        }


class AddPlace(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Add place executed"
        }


class CommandNotFound(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command not found"
        }
