from app.models import Comment

def test_comment(app):
  comment = Comment(
    text='Some awesome comment'
  )

  assert comment.text == 'Some awesome comment'