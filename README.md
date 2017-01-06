Please refer to requirements.txt  


Installation:  
1) Install all the dependencies  
2) `db_fill.py`. This step requires praw and fills the sample database with random images from Reddit.  
3) `run.py runserver`. Flask will output the url to be opened in browser.  

File structure:  
`run.py` - a script to run the application using built-in server.
`db_fill.py` - a script to fill database with random data from Reddit.
`spice` - main app directory, treated similar to a module.  
`spice/config.py` - app config, self-explanatory.  
`spice/database.py` - interface for adding and removing data from database, including adding pictures.  
`spice/misc.py` - various functions for adding pictures.  
`spice/models.py` - each class is a table, with keys to add relations.  
`spice/static/` - various files for templates.  
`spice/templates/` - web page templates.  
`spice/test.db/` - default database file.
`spice/views.py` - various functions for rendering pages.
