import json
from src.services.main_service import MainService
from src.services.input_validation import InputValidation
from src.data.user import User
from bson import json_util
from http import HTTPStatus
from jsonschema import ValidationError, validate
from src.services.input_validation import user_schema, user_schema_update

class UserService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users

    def create_user(self, user: dict) -> tuple:
        '''
        Create user
        
        Params:
            user: dict
        
        '''
        try:
            validate(instance=user, schema=user_schema)
        except ValidationError as e:
            return {"Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
        
        if self.users.find_one({'email': user['email']}) is not None:
            return {"Error": "User already exists"}, HTTPStatus.BAD_REQUEST
        
        new_user = User(user['name'], user['email'], user['password'], user['role'])
        self.users.insert_one(json.loads(new_user.toJSON()))
        return json.loads(json_util.dumps(user)), HTTPStatus.CREATED

    def get_user(self, user_email: str) -> tuple:
        '''
        Get user by email
        
        Params:
            user_email: str -> The email of the user to get
        '''
        data = self.users.find_one({'email': user_email})
        if data is None:
            return {"Error": "Can't find user with email: " + user_email}, HTTPStatus.NOT_FOUND
        return json.loads(json_util.dumps(data)), HTTPStatus.OK

    def update_user(self, user_email: str, new_user: dict) -> tuple:
        '''
        Update user by email
        
        Params:
            user_email: str -> The email of the user to update
            new_user: dict  -> The new user data
        '''
        try:
            validate(instance=new_user, schema=user_schema_update)
        except ValidationError as e:
            return {"Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST
            
        if new_user is None:
            return {"Error": "New user is missing"}, HTTPStatus.BAD_REQUEST
        
        user = self.users.find_one({'email': user_email})  # get user from database
        user = json.loads(json_util.dumps(user)) # convert to json

        user.update(new_user)  # update user with new_user
        
        self.users.update_one({'email': user_email}, {'$set': user})  # update user in database
        return '', HTTPStatus.NO_CONTENT
