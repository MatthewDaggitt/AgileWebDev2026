from flask import Config, Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.blueprints import main
    app.register_blueprint(main)

    return app

from app import routes
from app import models