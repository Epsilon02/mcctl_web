from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

from mcctlweb.config import Config

app = Flask(__name__)
socketio = SocketIO(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(Config)
db = SQLAlchemy(app)
Bootstrap(app)

from mcctlweb.filebrowser.routes import file_browser
from mcctlweb.main.routes import main
from mcctlweb.errors.handlers import errors

app.register_blueprint(file_browser)
app.register_blueprint(main)
app.register_blueprint(errors)
