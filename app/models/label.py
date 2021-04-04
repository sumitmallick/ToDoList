import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db
from .mixins.base import BaseMixin

class Label(BaseMixin, db.Model):
  __tablename__ = 'label'

  name = db.Column(db.Text, nullable=False)
  color = db.Column(db.String(8), nullable=False)

  board_id = db.Column(UUID(as_uuid=True), db.ForeignKey('board.id'), nullable=False)

  def __init__(self, name, color):
    self.name = name
    self.color = color

  def __repr__(self):
    return '<Label %r>' % self.name