from flask import Flask
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('application.instances.development')

from application import views

#def errorhandler(error):
#    """ Handle error """
#    if not isinstance(error, HTTPException):
#        error = InternalServerError()
#    return apology(error.name, error.code)

# Listen for errors
#for code in default_exceptions:
#    app.errorhandler(code)(errorhandler)
