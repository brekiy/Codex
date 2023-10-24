"""Routes for retrieving objects and articles related to rules."""
import flask

import codex

@codex.app.route("/traits", methods=["GET"])
def get_traits():
    traits = codex.mongo.db.traits.find();
    return flask.jsonify(traits)

@codex.app.route("/items", methods=["GET"])
def get_items():
    items = codex.mongo.db.items.find()
    return flask.jsonify(items)

@codex.app.route("/items/<category>", methods=["GET"])
def get_items_in_category(category):
    items = codex.mongo.db.items.find({"category": category})
    return flask.jsonify(items)