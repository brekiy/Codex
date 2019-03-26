import flask
from flask_pymongo import PyMongo

app = flask.Flask('codex')
app.config.from_object('codex.config')
mongo = PyMongo(app)
