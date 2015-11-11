from spice import application, models, db
import shutil
from spice.misc import imghdr, thumb, random_string, random_name
import io
import os
from collections import defaultdict

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
	category = models.Category.query.filter_by(name = cat).first()
	pic_uris = upload_pic(pic, application.config["PICS_DIR"], application.config["THUMBS_DIR"], (120, 120))
	picture = models.Picture(pic_uris[0], pic_uris[1])
	product = models.Product(name, category, price, picture)
	db.session.add(product)
	db.session.commit()

def upload_pic(pic, pic_dir, thumb_dir, thumb_size):
	buf = io.BytesIO()
	shutil.copyfileobj(pic, buf)
	buf.seek(0)
	ext = imghdr.what(buf)
	buf.seek(0)
	if not ext:
		raise TypeError("Unsupported image format")
	return_dir = application.config["APPLICATION_ROOT"]
	work_dir = os.path.dirname(__file__)
	os.chdir(work_dir)
	filename = random_name("png", length=12, dir=pic_dir)
	with open(pic_dir+"/"+filename, "wb") as f:
		shutil.copyfileobj(buf,f)
	buf.seek(0)
	if thumb_dir:
		thumb_filename = random_name("png", length=12, dir=thumb_dir)
		thumbnail = thumb(buf, thumb_size)
		thumbnail.seek(0)
		with open(thumb_dir+"/"+thumb_filename, "wb") as f:
			shutil.copyfileobj(thumbnail,f)
	else:
		thumb_filename = None
	return filename, thumb_filename

def get_categories():
	result = []
	super_cats = models.Supercategory.query.all()
	for super_cat in super_cats:
		item = {"name":super_cat.name,"subcats":[]}
		for sub_cat in models.Category.query.filter_by(super_cat_id = super_cat.id).all():
			item["subcats"].append((sub_cat.name,sub_cat.id))
		result.append(item)
	return result

def add_feedback(text, image):
	pic_uris = upload_pic(image, application.config["AVATAR_DIR"], application.config["AVATAR_THUMBS_DIR"], (20, 20))
	picture = models.Picture(pic_uris[0], pic_uris[1])
	comment = models.Feedback(text, picture)
	db.session.add(comment)
	db.session.commit()

def get_goods(cat_id):
	prods = models.Product.query.filter_by(category_id = cat_id).all()
	print("%s products for category" % len(prods))
	return prods

def get_feedback():
	fb = models.Feedback.query.all()
	result = []
	for comment in fb:
		result.append((comment.text, comment.avatar.thumb_uri))
	print(fb[0].avatar)
	return result

def reset():
	db.create_all()

