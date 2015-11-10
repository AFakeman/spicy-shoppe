from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
application = Flask(__name__)
db = SQLAlchemy(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

class Example(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140))
	def __init__(self):
		self.name = "hello"

db.create_all()

test_ex = Example()
test_ex2 = Example()
db.session.add(test_ex)
db.session.add(test_ex2)
db.session.commit()

@application.route('/')
def hello():
	Example.query.all()
	return(str(Example.query.all()))

application.run()