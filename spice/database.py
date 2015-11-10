from spice import application, models, db
import shutil
from spice.misc import imghdr, thumb, random_string, random_name
import io
import os
from collections import defaultdict

application.config["THUMBS_DIR"] = "static/thumbs"
application.config["PICS_DIR"] = "static/pics"

def add_category(name, super_name):
	super_cat = models.Supercategory.query.filter_by(name = super_name).first()
	print(super_cat)
	if not super_cat:
		super_cat = models.Supercategory(super_name)
		db.session.add(super_cat)
	if not(models.Category.query.filter_by(name = name).first()):
		cat = models.Category(name, super_cat)
		db.session.add(cat)
		db.session.commit()
	print(models.Supercategory.query.first())

def add_product(name, cat, price, pic):
	buf = io.BytesIO()
	shutil.copyfileobj(pic, buf)
	buf.seek(0)
	ext = imghdr.what(buf)
	buf.seek(0)
	if not ext:
		raise TypeError("Unsupported image format")
	return_dir = os.getcwd()
	work_dir = os.path.dirname(__file__)
	os.chdir(work_dir)
	filename = random_name("png", length=12, dir=application.config["PICS_DIR"])
	thumb_filename = random_name("png", length=12, dir=application.config["THUMBS_DIR"])
	with open(application.config["PICS_DIR"]+"/"+filename, "wb") as f:
		shutil.copyfileobj(buf,f)
	buf.seek(0)
	thumbnail = thumb(buf)
	thumbnail.seek(0)
	with open(application.config["THUMBS_DIR"]+"/"+thumb_filename, "wb") as f:
		shutil.copyfileobj(thumbnail,f)
	category = models.Category.query.filter_by(name = cat).first()
	picture = models.Picture(filename,thumb_filename)
	product = models.Product(name, category, price, picture)
	os.chdir(return_dir)
	db.session.add(product)
	db.session.commit()

def get_categories():
	result = []
	super_cats = models.Supercategory.query.all()
	for super_cat in super_cats:
		item = {"name":super_cat.name,"subcats":[]}
		for sub_cat in models.Category.query.filter_by(super_cat_id = super_cat.id).all():
			item["subcats"].append((sub_cat.name,sub_cat.id))
		result.append(item)
	return result

def get_goods(cat_id):
	#category = models.Category.query.filter_by(name = cat).first()
	return models.Product.query.filter_by(category_id = cat_id).all()

def reset():
	db.create_all()

