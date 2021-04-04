from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
  create_access_token,
  create_refresh_token
)

from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('email', help='This field cannot be blank', required = True)
parser.add_argument('password', help='This field cannot be blank', required = True)

class Register(Resource):
  def post(self):
    data = parser.parse_args()
    email = data['email']
    password = data['password']

    try:
      new_user = User(
        email=email,
        password=password
      )
      new_user.save()

      access_token = create_access_token(identity=email)
      refresh_token = create_refresh_token(identity=email)

      return {
        'access_token': access_token,
        'refresh_token': refresh_token
      }
    except IntegrityError:
      return {
        'message': {
          'email': 'Already in use'
        }
      }, HTTPStatus.CONFLICT

    return { 'message': 'Missing data' }, HTTPStatus.BAD_REQUEST