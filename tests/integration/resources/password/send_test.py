import json
from http import HTTPStatus

URL = '/api/password/send'

INVALID_USER = {
  'email': 'foo@bar.com'
}

NOT_FOUND_RES = {
  'message': {
    'email': 'Not found'
  }
}

SUCCESS_RES = {
  'message': 'Email has been sent'
}

def test_invalid_email(app, db, dummy_user):
  response = app.post(
    URL,
    data = json.dumps(INVALID_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.NOT_FOUND
  assert json.loads(response.data) == NOT_FOUND_RES

def test_valid_email(app, db, dummy_user):
  data = {
    'email': dummy_user.email
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.ACCEPTED
  assert 'token' in json.loads(response.data)
  assert json.loads(response.data).get('message') == SUCCESS_RES.get('message')