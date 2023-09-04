from flask import Flask
from flask_restful import Api
from REST.command_controller import CommandController
from REST.user_controller import UserControllerReadUpdate, UserControllerCreate
from REST.object_controller import ObjectControllerReadUpdate, ObjectControllerCreate
from REST.admin_controller import AdminControllerUsers, AdminControllerObjects, AdminControllerCommands


def create_app():
    app = Flask(__name__)
    app.config['ENV'] = 'development'
    return app


application = create_app()
api = Api(application)
# User Routes
api.add_resource(UserControllerReadUpdate, '/wastewise/users/<user_email>')
api.add_resource(UserControllerCreate, '/wastewise/users')

# Object Routes
api.add_resource(ObjectControllerReadUpdate, '/wastewise/objects/<object_id>')
api.add_resource(ObjectControllerCreate, '/wastewise/objects')

# Command Routes
api.add_resource(CommandController, '/wastewise/commands')

# Admin Routes
api.add_resource(AdminControllerUsers, '/wastewise/admin/users')
api.add_resource(AdminControllerObjects, '/wastewise/admin/objects')
api.add_resource(AdminControllerCommands, '/wastewise/admin/commands')

if __name__ == '__main__':
    application.run(debug=True)
