from src.services.commands.command_interface import ICommand
from src.services.rest.main_service import MainService
from http import HTTPStatus
from jsonschema import ValidationError, validate
from src.services.input_validation import direct_command_schema


class Direct(ICommand):
    def execute(self, data: dict):
        try:
            validate(instance=data, schema=direct_command_schema)
        except ValidationError as e:
            return {"Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
        lat = data.get("data").get("location").get("lat")
        lng = data.get("data").get("location").get("lng")
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
