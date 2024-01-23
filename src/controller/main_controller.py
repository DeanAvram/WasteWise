from flask import abort, make_response, jsonify


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def get_user_email(req):
        if req.args.get('email') is None:
            abort(make_response(jsonify(message="User email is missing"), 400))
        return req.args.get('email')

    @staticmethod
    def get_user_password(req):
        if req.args.get('password') is None:
            abort(make_response(jsonify(message="User password is missing"), 400))
        return req.args.get('password')


