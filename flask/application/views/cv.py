""" Flask-related imports """
from flask import render_template

""" nate.dev-related imports """
from application import app
from application.helpers import md2html

@app.route("/cv")
def cv() -> None:
    html : str = md2html("application/static/content/cv.md")
    return render_template("cv.html", html=html)
