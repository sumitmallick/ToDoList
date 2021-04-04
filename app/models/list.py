import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin

class List(BaseMixin, db.Model):
  __tablename__ = 'list'

  name = db.Column(db.Text, nullable=False)
  position = db.Column(db.Integer, nullable=False, default=1)

  board_id = db.Column(UUID(as_uuid=True), db.ForeignKey('board.id'), nullable=False)
  cards = db.relationship('Card', backref='list', lazy=True)

  def __init__(self, name, position):
    self.name = name
    self.position = position

  def __repr__(self):
    return '<List %r>' % self.name