from app.models import Label

def test_label(app):
  label = Label(
    name='Some awesome label',
    color='#ff0000'
  )

  assert label.name == 'Some awesome label'
  assert label.color == '#ff0000'