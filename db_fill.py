import re
import praw
import spice.database as database
from spice.misc import random_string
import urllib.request, urllib.error
import os
# re.match(r"https?://imgur.com/([a-zA-Z0-9]{7})", img_url) or re.match(r"https?://i.imgur.com/([a-zA-Z0-9]{7})", img_url)

Cats = [("Random","Reddit","pics"), \
		("Gaming", "Reddit", "gaming"), \
		("Animals", "Reddit", "AdviceAnimals")]

defaults = [("постоянно покупаю здесь спайс,никакого кидалова, ребят, обращайтесь", "http://placehold.it/350x150"),\
		("классно)) заказал проститутку, а она откинулась прям на мне, это было незабываемо))", "http://placehold.it/250/ff0000/000000"),\
		("подскажите ваш адрес, плз))", "http://placehold.it/250/0000ff/000000")]

def add_categories(defaults):
	Cats = defaults
	for cat in Cats:
		database.add_category(cat[0],cat[1])

def update_goods_from_Reddit(Cats):
	add_categories(Cats)
	red = praw.Reddit("Le Spicy Shoppe by Snoop v1.0")
	for cat in Cats:
		for sub in red.get_subreddit(cat[2]).get_hot(limit=20):
			img_url = sub.url
			if re.match(r".*(jpg|png)", img_url):
				name = sub.title[:20]
				category = cat[0]
				price = sub.score
				try:
					image = urllib.request.urlopen(img_url)
					database.add_product(name,category,price,image)
				except urllib.error.HTTPError:
					print(urllib.error)
				except TypeError:
					print(TypeError) 
			else:
				print(img_url)
	print("Done updating")

def update_feedback(defaults):
	for comment in defaults:
		try:
			image = urllib.request.urlopen(comment[1])
			database.add_feedback(comment[0], image)
		except urllib.error.HTTPError as e:
			print(e)

if (__name__ == '__main__'):
	database.reset()
	update_goods_from_Reddit(Cats)
	update_feedback(defaults)
	database.commit()