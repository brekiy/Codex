"""Routes for user accounts."""
import uuid
import hashlib
import flask
import flask_login

import codex

@codex.app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        print("received", flask.request.form)
        email = flask.request.form["email"].strip()
        password = flask.request.form["password"].strip()
        
        users = codex.mongo.db.users
        account = users.find_one({"email": email})
        if account is not None and hash_password(password) == account["password"]:
            # set current user and 
            flask_login.login_user(account)
            return flask.redirect(flask.url_for("index"))
        # report incorrect email/password
        return flask.redirect(flask.url_for("login", error=1))
    return flask.render_template("login.html", error = flask.request.args.get("error"))

@codex.app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "POST":
        email = flask.request.form["email"].strip()
        username = flask.request.form["username"].strip()
        password = flask.request.form["password"].strip()
        users = codex.mongo.db.users
        if users.find_one({"email": email, "username": username}) is not None:
            # report duplicate email/username
            return flask.redirect(flask.url_for("register", error=1))
        users.insert_one({"email": email, "username": username, "password": hash_password(password)})
    return flask.render_template("register.html")

def hash_password(password: str):
    algorithm = "sha512"
    # salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    # password_salted = salt + password
    hash_obj.update(password.encode("utf-8"))
    password_hash = hash_obj.hexdigest()
    return "$".join([algorithm, password_hash])
