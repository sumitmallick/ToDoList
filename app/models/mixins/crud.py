from app.models.base import db

# @source: https://github.com/mjhea0/flask-tracking/blob/master/app/mixins.py
class CRUDMixin(object):
  @classmethod
  def get_by_id(cls, id):
    return cls.query.get(id)

  @classmethod
  def create(cls, **kwargs):
    instance = cls(**kwargs)
    return instance.save()

  def update(self, commit=True, **kwargs):
    for attr, value in kwargs.items():
        setattr(self, attr, value)
    return commit and self.save() or self

  def save(self, commit=True):
    db.session.add(self)
    if commit:
        db.session.commit()
    return self

  def delete(self, commit=True):
    db.session.delete(self)
    return commit and db.session.commit()