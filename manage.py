import os
# from flask.ext.script import Manager  					# Python3
# from flask.ext.migrate import Migrate, MigrateCommand		# Python3

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flaskblockchain import app  # App is Flask(__name__), and db is Sqlalchemy(app)

app.config.from_object(os.environ['APP_SETTINGS'])

# migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()