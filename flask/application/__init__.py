""" Flask-related imports """
from flask import Flask
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

""" nate.dev-related imports """
from application.helpers import apology

# Configure application
app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('application.instances.development')

from application import views

def errorhandler(error):
    """ Handles errors """
    if not isinstance(error, HTTPException):
        error = InternalServerError()

    return apology(error.name, error.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
