"""Routes for user accounts."""
import flask
import flask_login

import codex

@codex.app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        # print("received", flask.request.form)
        email = flask.request.form["email"].strip()
        password = flask.request.form["password"].strip()
        users = codex.mongo.db.users
        account = users.find_one({"email": email})
        if account is not None and codex.utils.hash_password(password) == account["password"]:
            # set current user
            login_user = codex.schemas.user.User(str(account["_id"]), account["username"], account["email"])
            flask_login.login_user(login_user)
            return codex.utils.redirect_next_or_home(flask.request.args.get('next'));
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
        created = users.insert_one({"email": email, "username": username, "password": codex.utils.hash_password(password)})
        login_user = codex.schemas.user.User(str(created["_id"]), username, email)
        flask_login.login_user(login_user)
        return codex.utils.redirect_next_or_home(flask.request.args.get('next'));
    return flask.render_template("register.html", error = flask.request.args.get("error"))

@codex.app.route("/logout", methods=["POST"])
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("home"))

