"""Codex helper methods."""
import flask
from codex import app

# Session info

def check_login():
    """Check if a user is currently logged in."""
    if "username" in flask.session:
        return flask.session["username"]
    return None

# Database methods