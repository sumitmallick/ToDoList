import json
from http import HTTPStatus

URL = '/api/boards'

def test_forbidden(app, db, dummy_user):
  data = {
    'name': 'Some board',
    'owner_id': dummy_user.id.__str__()
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.UNAUTHORIZED

def test_invalid_params(app, db, authorized_user):
  data = {
    'name': 'Some board'
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json',
    headers={
      'Authorization': 'Bearer {}'.format(authorized_user.get('access_token'))
    }
  )

  error_response_json = {
    'message': {
      'owner_id': 'Required'
    }
  }

  assert response.status_code == HTTPStatus.BAD_REQUEST
  assert json.loads(response.data) == error_response_json

def test_valid_params(app, db, authorized_user):
  data = {
    'name': 'Some board',
    'owner_id': authorized_user.get('user').id.__str__()
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json',
    headers={
      'Authorization': 'Bearer {}'.format(authorized_user.get('access_token'))
    }
  )

  json_response = json.loads(response.data)

  assert response.status_code == HTTPStatus.CREATED
  assert 'board' in json_response
  assert 'id' in json_response.get('board')
  assert json_response.get('board').get('name') == data.get('name')
  assert json_response.get('board').get('owner_id') == data.get('owner_id')