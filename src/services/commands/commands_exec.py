import json

import pymongo
from flask import abort, make_response, jsonify

from src.data.object import Object
from src.services.commands.command_interface import ICommand
from src.services.rest.main_service import MainService
from http import HTTPStatus
from jsonschema import ValidationError, validate
from src.services.input_validation import direct_command_schema, history_command_schema, add_place_command_schema, \
    get_places_command_schema
from datetime import datetime, timedelta
from src.data.enum_periods import EnumPeriod


def validate_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return {
            "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
    except Exception as e:
        return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
    return None


class Direct(ICommand):
    def execute(self, data: dict, email: str):
        error = validate_schema(data, direct_command_schema)
        if error is not None:
            return error
        lng = data.get("data").get("location").get("lng")
        lat = data.get("data").get("location").get("lat")
        bin_type = data.get("data").get("bin_type")
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
                    "data.bin_type": bin_type,
                    "type": "recycle_facility",
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


def generate_query(data: dict):
    query = {"type": "classification", "active": True}
    if data.get("data").get("period") == EnumPeriod.WEEK.name:
        query["data.classification_time"] = {
            "$gte": datetime.now() - timedelta(weeks=1)
        }
    elif data.get("data").get("period") == EnumPeriod.MONTH.name:
        query["data.classification_time"] = {
            "$gte": datetime.now() - timedelta(days=30)
        }
    elif data.get("data").get("period") == EnumPeriod.YEAR.name:
        query["data.classification_time"] = {
            "$gte": datetime.now() - timedelta(days=365)
        }
    else:
        abort(make_response(jsonify(message="Period not found"), 400))
    return query


class History(ICommand):
    def execute(self, data: dict, email: str):
        # TODO: check why validation on enum doesn't work
        error = validate_schema(data, history_command_schema)
        if error is not None:
            return error
        # return all objects of type classification for the user in the relevant time frame
        query = generate_query(data)
        result = list(MainService().get_db().objects.find(query).sort('data.classification_time', pymongo.DESCENDING))
        if len(result) == 0:
            data = {"data": {
                "classification": "No recycle found",
                "classification_time": "Earth will be thankful if you will start to (:"
            }}
            result.append(data)
        return result, HTTPStatus.CREATED


class RecycleFacilities(ICommand):
    def execute(self, data: dict, email: str):
        error = validate_schema(data, get_places_command_schema)
        if error is not None:
            return error
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
            "type": "recycle_facility",
            "active": True
        }

        # return all places in the relevant radius
        result = list(MainService().get_db().objects.find(query))
        return result, HTTPStatus.CREATED


class AddPlace(ICommand):
    def execute(self, data: dict, email: str):
        error = validate_schema(data, add_place_command_schema)
        if error is not None:
            return error
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
