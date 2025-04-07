from flask import Flask 
from config import Config

app = Flask(__name__) # this is variable  whith name 'app' is part of app package 
app.config.from_object(Config)

from app import routes # importing from app package (the directory we are in)
