from flask import Blueprint
from ..controller.orders.concert_list_controller import ConcertListController

concert_list_bp = Blueprint("concert_list", __name__)
concert_list_controller = ConcertListController()

@concert_list_bp.route("/concert_list", methods=['GET'])
def get_dish():
    return concert_list_controller.get_all()

@concert_list_bp.route("/concert_list/<int:concert_list_id>", methods=['GET'])
def get_dish_by_id(concert_list_id):
    return concert_list_controller.get_by_id(concert_list_id)

@concert_list_bp.route("/concert_list", methods=['POST'])
def add_dish():
    return concert_list_controller.create()

@concert_list_bp.route("/concert_list/<int:concert_list_id>", methods=['PATCH'])
def update_actor(concert_list_id):
    return concert_list_controller.update(concert_list_id)

@concert_list_bp.route("/concert_list/<int:concert_list_id>", methods=['DELETE'])
def delete_dish(concert_list_id):
    return concert_list_controller.delete(concert_list_id)