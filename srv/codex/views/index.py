import flask
import codex

@codex.app.route("/", methods=["GET"])
def home():
  """Display the home page."""
  context = {}
  return flask.render_template("index.html", **context)