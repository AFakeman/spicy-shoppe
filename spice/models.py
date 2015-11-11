#two tables: one with category names, one with items

from spice import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140))
	category = db.relationship('Category', backref=db.backref('Product', lazy='dynamic'))
	price = db.Column(db.Integer)
	image = db.relationship('Picture', backref=db.backref('Product', lazy='dynamic'), uselist = False)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	picture_id = db.Column(db.Integer, db.ForeignKey('picture.id'))
	
	def __init__(self, name, cat, price, pic):
		self.name = name
		self.category = cat
		self.price = price
		self.image = pic

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140), unique = True)
	super_cat = db.relationship('Supercategory', backref=db.backref('Category', lazy='dynamic'))
	super_cat_id = db.Column(db.Integer, db.ForeignKey('supercategory.id'))
	
	def __init__(self, name, super_cat):
		self.name = name
		self.super_cat = super_cat

class Picture(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	img_uri = db.Column(db.String(140), unique = True)
	thumb_uri = db.Column(db.String(140), unique = True)
	
	def __init__(self,im,th):
		self.img_uri = im
		self.thumb_uri = th

class Supercategory(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140), unique = True)
	
	def __init__(self, name):
		self.name = name

class Feedback(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(140))
	avatar = db.relationship('Picture', backref=db.backref('Feedback', lazy='dynamic'), uselist = False)
	avatar_id = db.Column(db.Integer, db.ForeignKey('picture.id'))
	
	def __init__(self, text, avatar):
		self.text = text
		self.avatar = avatar