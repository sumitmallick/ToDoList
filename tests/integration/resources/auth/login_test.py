import json
from http import HTTPStatus

from app.models import User

URL = '/api/auth'

INVALID_USER = {
  'email': 'foo@bar.com',
  'password': 'password'
}

INVALID_CREDENTIALS_RES = {
  'message': 'Invalid credentials'
}

def test_invalid_email(app, db, dummy_user):
  response = app.post(
    URL,
    data = json.dumps(INVALID_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.FORBIDDEN
  assert json.loads(response.data) == INVALID_CREDENTIALS_RES

def test_invalid_password(app, db, dummy_user):
  data = {
    'email': dummy_user.email,
    'password': 'invalid password'
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.FORBIDDEN
  assert json.loads(response.data) == INVALID_CREDENTIALS_RES


def test_missing_params(app, db, dummy_user):
  data = {
    'email': INVALID_USER['email']
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  error_response_json = {
    'message': {
      'password': 'This field cannot be blank'
    }
  }

  assert response.status_code == HTTPStatus.BAD_REQUEST
  assert json.loads(response.data) == error_response_json

def test_valid_credentials(app, db, dummy_user):
  data = {
    'email': dummy_user.email,
    'password': 'password',
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.OK
  assert 'access_token' in json.loads(response.data)
  assert 'refresh_token' in json.loads(response.data)