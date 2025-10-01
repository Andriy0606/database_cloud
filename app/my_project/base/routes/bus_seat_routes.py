from flask import Blueprint
from ..controller.orders.bus_seat_controller import BusSeatController

bus_seat_bp = Blueprint("bus_seat", __name__)
bus_seat_controller = BusSeatController()

@bus_seat_bp.route("/bus_seat", methods=['GET'])
def get_dish():
    return bus_seat_controller.get_all()

@bus_seat_bp.route("/bus_seat/<int:bus_seat_id>", methods=['GET'])
def get_bus_seat_by_id(bus_seat_id):
    return bus_seat_controller.get_by_id(bus_seat_id)

@bus_seat_bp.route("/bus_seat", methods=['POST'])
def add_bus_seat():
    return bus_seat_controller.create()

@bus_seat_bp.route("/bus_seat/<int:bus_seat_id>", methods=['PATCH'])
def update_bus_seat(bus_seat_id):
    return bus_seat_controller.update(bus_seat_id)

@bus_seat_bp.route("/bus_seat/<int:bus_seat_id>", methods=['DELETE'])
def delete_bus_seat(bus_seat_id):
    return bus_seat_controller.delete(bus_seat_id)
