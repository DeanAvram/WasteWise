import os
from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

# Import your blueprints
from src.controller.objects_controller import objects
from src.controller.users_controller import users
from src.controller.command_controller import commands
from src.controller.admin_controller import admin
from src.controller.classification_controller import classification


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        CORS(app)
        app.config['CORS_HEADERS'] = 'Content-Type'
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY'),
        )
    else:
        app.config.from_mapping(test_config)

    # Swagger setup
    template = {
        "swagger": "2.0",
        "info": {
            "title": "WasteWise API",
            "description": "API for WasteWise project",
            "version": "1.0"
        },
        "basePath": "/wastewise",
    }

    swagger = Swagger(app, template=template)

    app.register_blueprint(objects)
    app.register_blueprint(users)
    app.register_blueprint(commands)
    app.register_blueprint(admin)
    app.register_blueprint(classification)

    return app
