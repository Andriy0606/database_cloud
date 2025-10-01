
from .concert_list_routes import concert_list_bp
from .bus_routes import bus_bp
from .bus_seat_routes import bus_seat_bp
from .feedback_routes import feedback_bp





def register_routes(app):
    app.register_blueprint(concert_list_bp, url_prefix="/api")
    app.register_blueprint(bus_bp, url_prefix="/api")
    app.register_blueprint(bus_seat_bp, url_prefix="/api")
    app.register_blueprint(feedback_bp, url_prefix="/api")


