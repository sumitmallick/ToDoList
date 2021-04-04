import uuid
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import db
from .crud import CRUDMixin

class BaseMixin(CRUDMixin, object):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  created_at = db.Column('created_at', db.DateTime, nullable=False)
  updated_at = db.Column('updated_at', db.DateTime, nullable=False)

@event.listens_for(BaseMixin, 'before_insert', propagate=True)
def before_insert(mapper, connection, instance):
  now = datetime.utcnow()
  instance.created_at = now
  instance.updated_at = now

@event.listens_for(BaseMixin, 'before_update', propagate=True)
def before_update(mapper, connection, instance):
  now = datetime.utcnow()
  instance.updated_at = now