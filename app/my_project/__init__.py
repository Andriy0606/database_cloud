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

    # ВАЖЛИВО: використовуємо Swagger 2.0 (а не openapi: 3.x)
    app.config['SWAGGER'] = {
        'uiversion': 3,          # сучасний інтерфейс
        'title': 'Concert Bus API'
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Concert Bus API",
            "version": "1.0.0",
            "description": "Документація до API курсового проєкту"
        },
        "basePath": "/",         # корінь
        "schemes": ["http"],     # якщо буде HTTPS — додасте "https"
        "paths": {}              # Flasgger сам підтягне з докстрінгів
    }

    Swagger(
        app,
        template=swagger_template,
        config={
            "specs": [
                {
                    "endpoint": 'apispec_1',
                    "route": '/apispec_1.json',
                    "rule_filter": lambda rule: True,
                    "model_filter": lambda tag: True,
                }
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/apidocs/"
        },
    )

    return app
