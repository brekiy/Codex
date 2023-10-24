"""Codex helper methods."""
import flask
import hashlib

# Session info

def check_login():
    """Check if a user is currently logged in."""
    if "username" in flask.session:
        return flask.session["username"]
    return None

def redirect_next_or_home(next_page: str):
    if next_page:
        return flask.redirect(flask.url_for(next_page))
    else:
        return flask.redirect(flask.url_for("home"))

def hash_password(password: str):
    algorithm = "sha512"
    # salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    # password_salted = salt + password
    hash_obj.update(password.encode("utf-8"))
    password_hash = hash_obj.hexdigest()
    return "$".join([algorithm, password_hash])