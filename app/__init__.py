from flask import Flask 

app = Flask(__name__) # this is variable  whith name 'app' is part of app package 

from app import routes # importing from app package (the directory we are in)
