from flask import Flask
from config.config import Config
from my_project.database import db
from my_project.base.routes import register_routes


from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    register_routes(app)

    # Swagger
    swagger_template = {
        "openapi": "3.0.3",
        "info": {
            "title": "Concert Bus API",
            "version": "1.0.0",
            "description": "Документація до API курсового проєкту"
        },
        "servers": [{"url": "/"}]
    }

    Swagger(app, template=swagger_template)

    return app
