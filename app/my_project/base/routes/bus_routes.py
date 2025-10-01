from flask import Blueprint
from ..controller.orders.bus_controller import BusController

bus_bp = Blueprint("bus", __name__)
bus_controller = BusController()

@bus_bp.route("/bus", methods=['GET'])
def get_bus():
    return bus_controller.get_all()

@bus_bp.route("/bus/<int:bus_id>", methods=['GET'])
def get_bus_by_id(bus_id):
    return bus_controller.get_by_id(bus_id)

@bus_bp.route("/bus", methods=['POST'])
def add_bus():
    return bus_controller.create()

@bus_bp.route("/bus/<int:bus_id>", methods=['PATCH'])
def update_bus(bus_id):
    return bus_controller.update(bus_id)

@bus_bp.route("/bus/<int:bus_id>", methods=['DELETE'])
def delete_bus(bus_id):
    return bus_controller.delete(bus_id)
