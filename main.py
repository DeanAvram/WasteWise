from flask import Flask
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from REST.command_controller import CommandController
from REST.user_controller import UserControllerReadUpdate, UserControllerCreate
from REST.object_controller import ObjectControllerReadUpdate, ObjectContollerCreate
from flask_pymongo import PyMongo


app = Flask(__name__)
api = Api(app)

# User Routes
api.add_resource(UserControllerReadUpdate, '/wastewize/users/<user_email>')
api.add_resource(UserControllerCreate, '/wastewize/users')

# Object Routes
api.add_resource(ObjectControllerReadUpdate, '/wastewize/objects/<object_id>')
api.add_resource(ObjectContollerCreate, '/wastewize/objects')

# Command Routes
api.add_resource(CommandController, '/wastewize/commands')

app.run()
