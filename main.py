from flask import Flask
from flask_restful import Api
from REST.command_controller import CommandController
from REST.user_controller import UserControllerReadUpdate, UserControllerCreate
from REST.object_controller import ObjectControllerReadUpdate, ObjectContollerCreate
from REST.admin_controller import AdminControllerUsers, AdminControllerObjects, AdminControllerCommands


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

# Admin Routes
api.add_resource(AdminControllerUsers, '/wastewize/admin/users')
api.add_resource(AdminControllerObjects, '/wastewize/admin/objects')
api.add_resource(AdminControllerCommands, '/wastewize/admin/commands')

app.run()
