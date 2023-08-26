from flask import Flask
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from REST.user_controller import UserControllerReadUpdate, UserControllerCreate
from flask_pymongo import PyMongo


app = Flask(__name__)
api = Api(app)

api.add_resource(UserControllerReadUpdate, '/wastewize/users/<user_id>')
api.add_resource(UserControllerCreate, '/wastewize/users')
app.run()
