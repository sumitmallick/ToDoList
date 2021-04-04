from app.models import Card

def test_card(app):
  card = Card(
    name='My card',
    description='Some awesome card',
    position=1
  )

  assert card.name == 'My card'
  assert card.description == 'Some awesome card'
  assert card.position == 1