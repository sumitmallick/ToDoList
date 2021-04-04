import json
from http import HTTPStatus

URL = '/api/auth/register'

NEW_USER = {
  'email': 'joe@doe.com',
  'password': 'password123'
}

CONFLICT_RES = {
  'message': {
    'email': 'Already in use'
  }
}

def test_existing_user(app, db, dummy_user):
  data = {
    'email': dummy_user.email,
    'password': 'password',
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.CONFLICT
  assert json.loads(response.data) == CONFLICT_RES

def test_new_user(app, db, dummy_user):
  response = app.post(
    URL,
    data = json.dumps(NEW_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.OK
  assert 'access_token' in json.loads(response.data)
  assert 'refresh_token' in json.loads(response.data)