from app.models import Board

def test_board(app, db, dummy_user):
  board = Board(
    name='My board',
    owner_id=dummy_user.id
  )

  assert board.name == 'My board'
  assert board.owner_id == dummy_user.id