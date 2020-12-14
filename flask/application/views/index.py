from flask import render_template

from application import app
from application.helpers import md2html

@app.route("/")
def about():
    html = md2html("application/static/content/about.md")
    return render_template("index.html", html=html)

