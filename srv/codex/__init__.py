import flask
import flask_login
import flask_pymongo



app = flask.Flask('codex')
app.config.from_object('codex.config')
mongo = flask_pymongo.PyMongo(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from codex import views

@login_manager.user_loader
def load_user(id: str):
    user = mongo.users.find_one({"id": id})
    if user:
        return app.schema.user.User(user["id"], user["username"], user["email"])
    return None