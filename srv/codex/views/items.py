"""Routes for retrieving objects and articles related to items."""
import flask
import codex
import bson.json_util

@codex.app.route("/traits", methods=["GET"])
def get_traits():
    traits = codex.mongo.db.traits.find();
    data = process_documents(traits)
    return data

@codex.app.route("/traits", methods=["POST"])
def add_traits():
    # request body: { "traits": [ {"name", "description"} ]}
    # fail entire request if expected format not received, dont bother with partial work
    body = flask.request.get_json(silent=False)
    if "traits" not in body or type(body["traits"]) != list:
        return "Bad request", 400
    to_commit = []
    for trait in body["traits"]:
        if any(x not in trait for x in ["name", "description"]):
            return "Bad request", 400
        to_commit.append({"name": trait["name"], "description": trait["description"]})
    codex.mongo.db.traits.insert_many(to_commit)
    return "Created", 201

@codex.app.route("/items/<category>", methods=["GET"])
def get_items_in_category(category):
    # valid categories are: misc, armor, meleeweapons, rangedweapons
    if category not in ["misc", "armor", "meleeweapons", "rangedweapons"]:
        return "Bad request", 400
    
    items = getattr(codex.mongo.db, category_to_collection(category)).find()
    data = process_documents(items)
    return data

def category_to_collection(category: str) -> str:
    if category == "misc":
        return "misc_items"
    elif category == "meleeweapons":
        return "melee_weapons"
    elif category == "rangedweapons":
        return "ranged_weapons"
    else:
        return category
    
def process_documents(cursor) -> str:
    items = list(cursor)
    for i in items:
        i["_id"] = str(i["_id"])
    data = bson.json_util.dumps(items, indent=2)
    return data
