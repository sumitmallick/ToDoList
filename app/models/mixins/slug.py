from slugify import slugify

from app.models.base import db

def generate_slug(context):
  return slugify(context.get_current_parameters().get('name'))

class SlugifiedMixin(object):
  slug = db.Column(
    db.Text,
    unique=True,
    nullable=False,
    default=generate_slug,
    onupdate=generate_slug
  )