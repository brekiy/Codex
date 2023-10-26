import flask
import flask_login
import flask_pymongo


app = flask.Flask('codex')
app.config.from_object('codex.config')
mongo = flask_pymongo.PyMongo(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from codex import views, utils, schemas

@login_manager.user_loader
def load_user(id: str):
    user = mongo.db.users.find_one({"id": id})
    if user:
        return schemas.user.User(user["id"], user["username"], user["email"])
    return None
