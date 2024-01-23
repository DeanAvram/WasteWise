import json

from src.data.object import Object
from src.services.commands.command_interface import ICommand
from src.services.rest.main_service import MainService
from http import HTTPStatus
from jsonschema import ValidationError, validate
from src.services.input_validation import direct_command_schema, history_command_schema, add_place_command_schema, get_places_command_schema
from datetime import datetime, timedelta
from src.data.enum_periods import EnumPeriod


class Direct(ICommand):
    def execute(self, data: dict, email: str):
        try:
            validate(instance=data, schema=direct_command_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
        lng = data.get("data").get("location").get("lng")
        lat = data.get("data").get("location").get("lat")
        reference_location = {
            "type": "Point",
            "coordinates": [lng, lat]
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
                # Filter only objects of type place that are active
                "$match": {
                    "type": "place",
                    "active": True
                }
            },
            {
                "$limit": 1  # Limit the result to one document - the closest one
            }
        ]

        result = list(MainService().get_db().objects.aggregate(pipeline))
        if len(result) == 0:
            return {"Error": "No objects found"}, HTTPStatus.NOT_FOUND
        return result[0], HTTPStatus.CREATED


class History(ICommand):
    def execute(self, data: dict, email: str):
        # TODO: check why validation on enum doesn't work
        try:
            validate(instance=data, schema=history_command_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
        # return all objects of type classification for the user in the relevant time frame
        result = list(MainService().get_db().objects.find({"type": "classification", "created_by": email}))
        today = datetime.now()
        last_week = today - timedelta(weeks=1)
        last_month = today - timedelta(days=30)
        last_year = today - timedelta(days=365)
        if data.get("data").get("period") == EnumPeriod.WEEK.name:
            result = list(MainService().get_db().objects.find({"type": "classification", "created_by": email,
                                                               "active": True,
                                                               "data.classification_time": {
                                                                   "$gte": last_week
                                                               }}))
        elif data.get("data").get("period") == EnumPeriod.MONTH.name:
            result = list(MainService().get_db().objects.find({"type": "classification", "created_by": email,
                                                               "active": True,
                                                               "data.classification_time": {
                                                                   "$gte": last_month
                                                               }}))
        elif data.get("data").get("period") == EnumPeriod.YEAR.name:
            result = list(MainService().get_db().objects.find({"type": "classification", "created_by": email,
                                                               "active": True,
                                                               "data.classification_time": {
                                                                   "$gte": last_year
                                                               }}))
        elif data.get("data").get("period") == EnumPeriod.ALL.name:
            result = list(MainService().get_db().objects.find({"type": "classification", "created_by": email}))
        else:
            return {"Error": "Period not found"}, HTTPStatus.BAD_REQUEST
        if len(result) == 0:
            data = {"data": {
                "classification": "No recycle found",
                "classification_time": "Earth will be thankful if you will start to (:"
            }}
            result.append(data)
        return result, HTTPStatus.CREATED


class Places(ICommand):
    def execute(self, data: dict, email: str):
        try:
            validate(instance=data, schema=get_places_command_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
        # Extract the location from the request
        lng = data.get("data").get("location").get("lng")
        lat = data.get("data").get("location").get("lat")
        # Create a GeoJSON object
        curr_location = {
            "type": "Point",
            "coordinates": [lng, lat]
        }
        # Extract the max distance from the request
        radius = data.get("data").get("radius")
        query = {
            "data.location.coordinates": {
                "$geoWithin": {
                    "$centerSphere": [curr_location["coordinates"], radius / 6371]
                }
            },
            "type": "place",
            "active": True
        }

        # return all places in the relevant radius
        result = list(MainService().get_db().objects.find(query))
        return result, HTTPStatus.CREATED


class AddPlace(ICommand):
    def execute(self, data: dict, email: str):
        try:
            validate(instance=data, schema=add_place_command_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
        # Extract the location from the request
        lng = data.get("data").get("location").get("lng")
        lat = data.get("data").get("location").get("lat")
        # Create a GeoJSON object

        # Create a new object
        obj = Object("place", email)
        obj.data = {
            "name": data.get("data").get("name"),
            "location": {
                "coordinates": [lng, lat]
            }
        }
        # Insert the object into the database
        MainService().get_db().objects.insert_one(json.loads(obj.toJSON()))
        return json.loads(obj.toJSON()), HTTPStatus.CREATED


class CommandNotFound(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command not found"
        }


class General(ICommand):
    def execute(self, data: dict, email: str):
        return {
            "email": email,
            "data": data
        }