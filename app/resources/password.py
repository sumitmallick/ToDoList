from http import HTTPStatus

from flask import current_app, request, make_response, jsonify
from itsdangerous import TimestampSigner, SignatureExpired

from .base import api_bp
from app.models import User

@api_bp.route('/password/send', methods=['POST'])
def send():
  pass_secret = current_app.config.get('PASS_SECRET_KEY')
  pass_token_age = current_app.config.get('PASS_TOKEN_AGE')
  test_mode = current_app.config.get('TESTING')

  email = request.json.get('email')
  user = User.get_by_email(email)

  if user:
    singer = TimestampSigner(pass_secret)
    token_bytes = singer.sign(user.email)
    token = token_bytes.decode('utf-8')

    # Send token only for testing purposes
    if test_mode == True:
      return make_response(
        jsonify({
          'message': 'Email has been sent',
          'token': token
        }),
        HTTPStatus.ACCEPTED
      )

    # TODO: add sending email
    current_app.logger.info('Reset password link: /password/reset?token=%s', token)

    return make_response(
      jsonify({
        'message': 'Email has been sent'
      }),
      HTTPStatus.ACCEPTED
    )

  return make_response(
    jsonify({
      'message': {
        'email': 'Not found'
      }
    }),
    HTTPStatus.NOT_FOUND
  )

@api_bp.route('/password/reset', methods=['POST'])
def reset():
  pass_secret = current_app.config.get('PASS_SECRET_KEY')
  pass_token_age = current_app.config.get('PASS_TOKEN_AGE')
  test_mode = current_app.config.get('TESTING')

  token = request.json.get('token')
  old_password = request.json.get('old_password')
  new_password = request.json.get('new_password')

  singer = TimestampSigner(pass_secret)

  try:
    email_bytes = singer.unsign(token.encode(), max_age=pass_token_age)
    email = email_bytes.decode('utf-8')
    user = User.get_by_email(email)

    if user and user.password_match(old_password):
      user.update(
        password=new_password
      )

      return make_response(
        jsonify({
          'message': 'Password reseted!'
        }),
        HTTPStatus.CREATED
      )

    return make_response(
      jsonify({
        'message': {
          'email': 'Not found'
        }
      }),
      HTTPStatus.NOT_FOUND
    )

  except SignatureExpired:
    return make_response(
      jsonify({
        'message': {
          'token': 'Expired'
        }
      }),
      HTTPStatus.FORBIDDEN
    )
  except:
    return make_response(
      jsonify({
        'message': {
          'token': 'Invalid value'
        }
      }),
      HTTPStatus.BAD_REQUEST
    )