from flask import Flask
from config import Config
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
#socketio = SocketIO(app, cors_allowed_origins='http://localhost:8080')
socketio = SocketIO(app, cors_allowed_origins='*')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
ma = Marshmallow(app)
cors = CORS(app)

from app import routes, models