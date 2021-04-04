import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin

labels = db.Table('card_label',
  db.Column('card_id', UUID(as_uuid=True), db.ForeignKey('card.id'), primary_key=True),
  db.Column('label_id', UUID(as_uuid=True), db.ForeignKey('label.id'), primary_key=True)
)

class Card(BaseMixin, db.Model):
  __tablename__ = 'card'

  name = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)
  position = db.Column(db.Integer, nullable=False, default=1)

  comments = db.relationship('Comment', backref='card', lazy=True)
  board_id = db.Column(UUID(as_uuid=True), db.ForeignKey('board.id'), nullable=False)
  list_id = db.Column(UUID(as_uuid=True), db.ForeignKey('list.id'), nullable=False)
  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)

  labels = db.relationship('Label', secondary=labels, lazy='subquery',
    backref=db.backref('card', lazy=True))

  def __init__(self, name, description, position):
    self.name = name
    self.description = description
    self.position = position

  def __repr__(self):
    return '<Card %r>' % self.name