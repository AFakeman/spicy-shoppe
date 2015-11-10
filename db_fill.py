import re
import praw
import spice.database as database
from spice.misc import random_string
import urllib.request
import os

def add_categories(defaults):
	Cats = defaults
	for cat in Cats:
		database.add_category(cat[0],cat[1])

def update_goods():
	Cats = [("Random","Reddit","pics"), \
			("Gaming", "Reddit", "gaming"), \
			("Animals", "Reddit", "AdviceAnimals")]
	add_categories(Cats)
	red = praw.Reddit("Le Spicy Shoppe by Snoop v1.0")
	for cat in Cats:
		for sub in red.get_subreddit(cat[2]).get_hot(limit=20):
			img_url = sub.url
			if re.match(r"https?://imgur.com/([a-zA-Z0-9]{7})", img_url) or re.match(r"https?://i.imgur.com/([a-zA-Z0-9]{7})", img_url):
				name = sub.title[:20]
				category = cat[0]
				price = sub.score
				image = urllib.request.urlopen(img_url)
				try:
					database.add_product(name,category,price,image)
				except:
					print("Invalid file, skiping")
			else:
				print(img_url)
	print("Done updating")
