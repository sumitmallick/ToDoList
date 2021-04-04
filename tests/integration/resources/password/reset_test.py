import json
import time
from http import HTTPStatus

URL = '/api/password/reset'

INVALID_USER = {
  'email': 'foo@bar.com'
}

EXPIRED_TOKEN_RES = {
  'message': {
    'token': 'Expired'
  }
}

INVALID_TOKEN_RES = {
  'message': {
    'token': 'Invalid value'
  }
}

SUCCESS_RES = {
  'message': 'Password reseted!'
}

def test_expired_token(app, db, dummy_user):
  send_response = app.post(
    '/api/password/send',
    data = json.dumps({
      'email': dummy_user.email
    }),
    content_type = 'application/json'
  )

  # Sleep for 2 seconds to invalidate token
  time.sleep(2)

  data = {
    'token': json.loads(send_response.data).get('token'),
    'old_password': 'password',
    'new_password': 'password123'
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.FORBIDDEN
  assert json.loads(response.data) == EXPIRED_TOKEN_RES

def test_invalid_token(app, db, dummy_user):
  data = {
    'token': 'invalid token',
    'old_password': 'password',
    'new_password': 'password123'
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.BAD_REQUEST
  assert json.loads(response.data) == INVALID_TOKEN_RES

def test_successful_reset(app, db, dummy_user):
  send_response = app.post(
    '/api/password/send',
    data = json.dumps({
      'email': dummy_user.email
    }),
    content_type = 'application/json'
  )

  data = {
    'token': json.loads(send_response.data).get('token'),
    'old_password': 'password',
    'new_password': 'password123'
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.CREATED
  assert json.loads(response.data) == SUCCESS_RES