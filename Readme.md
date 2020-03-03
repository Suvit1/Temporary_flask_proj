This is a Flask server project .

The initial start app function for a flask server here in test.py

db_init.py is used to initialise the police database for sql and has to be executed only once to create the db and tables

Major implementation of the code is in app folder (Standard in flask)

app
  - routes.py consists of routing for different paths for the server and decides what action to take on entering a certain route
  - db_functions.py consists of the table data store and retreival wrappers on sqlite db and also consists of hash functions that are created 
    by hashing the file stored in db
  - __init__.py is initializer for flask
  
  - templates consists of the html and csv files to be displayed in frontend . Of these , site.html consists of the blockchain frontend while
    rest are pages linked for Submitting an FIR and checking the status
