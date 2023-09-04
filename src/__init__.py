import os
from flask import Flask

from src.controller.objects_controller import objects
from src.controller.users_controller import users
from src.controller.command_controller import commands
from src.controller.admin_controller import admin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SEKRET_KEY=os.environ.get('SECRET_KEY'),
        )
    else:
        app.config.from_mapping(test_config)
    
    
    app.register_blueprint(objects)
    app.register_blueprint(users)
    app.register_blueprint(commands)
    app.register_blueprint(admin)

    return app