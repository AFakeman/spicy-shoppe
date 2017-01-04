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

defaults = [("постоянно покупаю здесь спайс,никакого кидалова, ребят, обращайтесь", "http://imgs.xkcd.com/comics/artifacts.png"),\
        ("классно)) заказал проститутку, а она откинулась прям на мне, это было незабываемо))", "http://imgs.xkcd.com/comics/artifacts.png"),\
        ("подскажите ваш адрес, плз))", "http://imgs.xkcd.com/comics/artifacts.png")]

def add_categories(defaults):
    Cats = defaults
    for cat in Cats:
        database.add_category(cat[0],cat[1])

def update_goods_from_Reddit(Cats):
    add_categories(Cats)
    red = praw.Reddit(client_id = 'rwK_HKJFy9T2qQ', client_secret = 'XIoCIGBaXmwEOJLIBp6KNeeNLUk', user_agent = 'keks')
    for cat in Cats:
        for sub in red.subreddit(cat[2]).hot(limit=20):
            img_url = sub.url
            if re.match(r".*(jpg|png)", img_url):
                name = sub.title[:20]
                category = cat[0]
                price = sub.score
                try:
                    image = urllib.request.urlopen(img_url)
                    database.add_product(name,category,price,image)
                except urllib.error.HTTPError:
                    print("Error during adding goods")
                    print(urllib.error)
                except TypeError:
                    print(TypeError) 
    print("Done updating")

def update_feedback(defaults):
    for comment in defaults:
        try:
            image = urllib.request.urlopen(comment[1])
            database.add_feedback(comment[0], image)
        except urllib.error.HTTPError as e:
            print("Error during adding feedback")
            print(e)

if (__name__ == '__main__'):
    database.reset()
    update_goods_from_Reddit(Cats)
    update_feedback(defaults)
    database.commit()