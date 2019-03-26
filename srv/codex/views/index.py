import flask
import codex

@codex.app.route("/", methods=["GET"])
def home_page():
  """Display the home page."""
  context = {}
  username = codex.model.check_login()
  if username is not None:
    context["username"] = username
  return flask.render_template("home.html", **context)