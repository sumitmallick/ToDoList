from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager

api_bp = Blueprint('api', __name__)

api = Api(api_bp)
jwt = JWTManager()