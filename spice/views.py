from spice import application, database
from flask import render_template, send_from_directory

@application.route('/thumbs/<image>')
def thumb(image):
	print(image)
	return send_from_directory(application.config["THUMBS_DIR"], image)

@application.route('/avatar_thumbs/<image>')
def avatar_thumb(image):
	print(image)
	return send_from_directory(application.config["AVATAR_THUMBS_DIR"], image)

@application.route('/')
def hello():
	return(render_template("index.html", cats = database.get_categories(), feedback = database.get_feedback()))

@application.route('/category/<cat_id>')
def show_wares(cat_id):
	return(render_template("itemlist.html", cats = database.get_categories(), products = database.get_goods(cat_id)))