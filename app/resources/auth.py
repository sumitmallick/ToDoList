from http import HTTPStatus

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
  create_access_token,
  create_refresh_token
)

from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('email', help='This field cannot be blank', required = True)
parser.add_argument('password', help='This field cannot be blank', required = True)

class Auth(Resource):
  def post(self):
    data = parser.parse_args()
    email = data['email']
    password = data['password']
    current_user = User.get_by_email(email)

    if current_user and current_user.password_match(password):
      access_token = create_access_token(identity=email)
      refresh_token = create_refresh_token(identity=email)

      return {
        'access_token': access_token,
        'refresh_token': refresh_token
      }

    return { 'message': 'Invalid credentials' }, HTTPStatus.FORBIDDEN