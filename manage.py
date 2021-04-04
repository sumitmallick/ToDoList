import os
from flask_script import Manager
from flask_migrate import MigrateCommand

from app import migrate, create_app
from app.models import db

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def drop_db():
  print('Dropping database...')
  db.drop_all()
  db.session.commit()
  print('Done!')

@manager.command
def recreate_db():
  print('Recreating database...')
  db.drop_all()
  db.create_all()
  db.session.commit()
  print('Done!')

if __name__ == '__main__':
  manager.run()