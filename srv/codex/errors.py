from flask import render_template
from codex import app

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/404.html'), 404