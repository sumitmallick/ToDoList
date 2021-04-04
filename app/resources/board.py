import uuid
from http import HTTPStatus

from flask_restful import Resource, reqparse, fields, marshal

from flask_jwt_extended import (
  create_access_token,
  create_refresh_token,
  jwt_required,
  jwt_refresh_token_required,
  get_jwt_identity,
  get_raw_jwt
)

from app.models import Board as BoardModel

parser = reqparse.RequestParser()
parser.add_argument('name', help='Required', required=True)
parser.add_argument('owner_id', help='Required', required=True)

permitted = {
  'id': fields.String,
  'name': fields.String,
  'owner_id': fields.String
}

class Board(Resource):
  method_decorators = [jwt_required]

  def post(self):
    data = parser.parse_args()
    name = data['name']
    owner_id = data['owner_id']

    try:
      new_board = BoardModel(
        name=name,
        owner_id=uuid.UUID(owner_id)
      )

      new_board.save()

      return {
        'board': marshal(new_board, permitted)
      }, HTTPStatus.CREATED
    except Exception as error:
      return {
        'message': str(error)
      }, HTTPStatus.INTERNAL_SERVER_ERROR