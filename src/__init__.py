from flask import Flask
from flask_restful import Api
from src.REST.admin_controller import AdminControllerCommands, AdminControllerObjects, AdminControllerUsers
from src.REST.command_controller import CommandController
from src.REST.object_controller import ObjectContollerCreate, ObjectControllerReadUpdate

from src.REST.user_controller import UserControllerCreate, UserControllerReadUpdate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SEKRET_KEY='dev',
        )
    else:
        app.config.from_mapping(test_config)
    
    api = Api(app)
    
    # User Routes
    api.add_resource(UserControllerReadUpdate, '/wastewise/users/<user_email>')
    api.add_resource(UserControllerCreate, '/wastewise/users')

    # Object Routes
    api.add_resource(ObjectControllerReadUpdate, '/wastewise/objects/<object_id>')
    api.add_resource(ObjectContollerCreate, '/wastewise/objects')

    # Command Routes
    api.add_resource(CommandController, '/wastewise/commands')

    # Admin Routes
    api.add_resource(AdminControllerUsers, '/wastewise/admin/users')
    api.add_resource(AdminControllerObjects, '/wastewise/admin/objects')
    api.add_resource(AdminControllerCommands, '/wastewise/admin/commands')

    return app