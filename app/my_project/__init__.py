from flask import Flask
from my_project.database import db
from my_project.base.routes.__init__ import register_routes
from config.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)

    return app
