import os

from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

from app import views