import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin
from .mixins.slug import SlugifiedMixin

class Board(BaseMixin, SlugifiedMixin, db.Model):
  __tablename__ = 'board'

  name = db.Column(db.Text, nullable=False)

  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
  lists = db.relationship('List', backref='board', lazy=True)
  labels = db.relationship('Label', backref='board', lazy=True)
  cards = db.relationship('Card', backref='board', lazy=True)

  def __init__(self, name, owner_id):
    self.name = name
    self.owner_id = owner_id

  def __repr__(self):
    return '<Board %r>' % self.name