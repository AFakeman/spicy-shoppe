Requirements:  
1) Python 3.4  
2) Flask (tested with 0.10.1)  
3) Flask-Script (tested with 2.0.5)
4) Flask-SQLAlchemy (tested with 2.0)
5) praw (tested with 3.2.1)

Installation:  
1) Install all the dependencies  
2) `db_fill.py`. This step requires praw and fills the sample database with random images from Reddit.  
3) `run.py runserver`. Flask will output the url to be opened in browser.  

File structure:  
`spice` - main app directory, treated similar to a module.  
`spice/config.py` - app config, self-explanatory.  
`spice/database.py` - interface for adding and removing data from database, including adding pictures.  
`spice/misc.py` - various functions for adding pictures.  
`spice/models.py` - each class is a table, with keys to add relations.  
`spice/static/` - various files for templates.  
`spice/templates/` - web page templates.  
`spice/test.db/` - default database file.
`spice/views.py` - various functions for rendering pages.