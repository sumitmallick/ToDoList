from app.models import User

def test_user(app):
  user = User(
    email='bruce@wright.com',
    password='password123'
  )

  user.first_name = 'Bruce'
  user.last_name = 'Wright'

  assert user.first_name == 'Bruce'
  assert user.last_name == 'Wright'
  assert user.email == 'bruce@wright.com'
  assert user._password != 'password123'