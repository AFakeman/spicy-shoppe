from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
import os

application = Flask(__name__)
application.debug = False
application.use_reloader = False
db = SQLAlchemy(application)
manager = Manager(application)
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

for dir in os.path.split(application.config["AVATAR_THUMBS_DIR"]):
	if not os.path.isdir(dir):
		os.mkdir(dir)
	os.chdir(dir)
os.chdir(application.config['APPLICATION_ROOT'])

for dir in os.path.split(application.config["AVATAR_DIR"]):
	if not os.path.isdir(dir):
		os.mkdir(dir)
	os.chdir(dir)
os.chdir(application.config['APPLICATION_ROOT'])