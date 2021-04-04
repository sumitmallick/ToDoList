import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin

class Comment(BaseMixin, db.Model):
  __tablename__ = 'comment'

  text = db.Column(db.Text, nullable=False)

  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
  card_id = db.Column(UUID(as_uuid=True), db.ForeignKey('card.id'), nullable=False)

  def __init__(self, text):
    self.text = text

  def __repr__(self):
    return '<Comment %r>' % self.id