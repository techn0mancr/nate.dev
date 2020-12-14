from flask import render_template

from application import app
from application.helpers import md2html

@app.route("/cv")
def cv():
    html = md2html("application/static/content/cv.md")
    return render_template("cv.html", html=html)
