""" Flask-related imports """
from flask import render_template

""" nate.dev-related imports """
from application import app
from application.helpers import md2html

@app.route("/")
def about() -> None:
    html : str = md2html("application/static/content/about.md")
    return render_template("index.html", html=html)

