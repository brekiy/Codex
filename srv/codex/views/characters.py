import flask
import codex

@codex.app.route("/characters/<char_id>", methods=["GET"])
def get_character_by_id(char_id: str):
    character = codex.mongo.db.characters.find({"_id": char_id})
    return flask.jsonify(character)

@codex.app.route("/characters/create/user/<user_id>", methods=["POST"])
def create_character_blank(user_id):
    data = flask.request.data
    character = {
        "user_id": user_id,
        "name": data["name"],
        "biography": {
            "backstory": data["backstory"],
            "goals": data["goals"],
            "personality": data["personality"]
        },
        "species": data["species"],
        "spamfic": {
            "spr": data["spamfic"]["spr"],
            "per": data["spamfic"]["per"],
            "agi": data["spamfic"]["agi"],
            "mgt": data["spamfic"]["mgt"],
            "for": data["spamfic"]["for"],
            "int": data["spamfic"]["int"],
            "chr": data["spamfic"]["chr"],
        },
        "skills": {},
        "feats": {},
        "money": data["money"],
        "inventory": []
    }
    codex.mongo.db.characters.insert_one(character)

def validate_character_input(data) -> bool:
    top_level = ["name", "backstory", "goals", "personality", "species", 
                 "spamfic", "skills", "feats", "money", "inventory"]
    spamfic = ["spr", "per", "agi", "mgt", "for", "int", "chr"]

    # top-level check
    if any(x not in data for x in top_level):
        return False
    if any(x not in data["spamfic"] for x in spamfic):
        return False
    return True