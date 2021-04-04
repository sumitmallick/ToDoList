from .base import api, api_bp, jwt
from .auth import Auth
from .register import Register
from .board import Board

import app.resources.password

api.add_resource(Auth, '/auth')
api.add_resource(Register, '/auth/register')
api.add_resource(Board, '/boards')

__all__ = [
  'api',
  'api_bp',
  'jwt',
  'Auth',
  'Register'
]