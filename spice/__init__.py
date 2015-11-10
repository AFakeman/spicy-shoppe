from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

application = Flask(__name__)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)
application.config.from_pyfile('config.py')
application.config['APPLICATION_ROOT'] = os.path.dirname(__file__)

import spice.views

os.chdir(os.path.dirname(__file__))
for dir in os.path.split(application.config["THUMBS_DIR"]):
	if not os.path.isdir(dir):
		os.mkdir(dir)
	os.chdir(dir)
os.chdir(application.config['APPLICATION_ROOT'])

for dir in os.path.split(application.config["PICS_DIR"]):
	if not os.path.isdir(dir):
		os.mkdir(dir)
	os.chdir(dir)
os.chdir(application.config['APPLICATION_ROOT'])
#import spice.db_fill

