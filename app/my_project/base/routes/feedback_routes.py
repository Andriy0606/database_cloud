from flask import Blueprint
from ..controller.orders.feedback_controller import FeedbackController

feedback_bp = Blueprint("feedback", __name__)
feedback_controller = FeedbackController()

@feedback_bp.route("/feedback", methods=['GET'])
def get_dish():
    return feedback_controller.get_all()

@feedback_bp.route("/feedback/<int:feedback_id>", methods=['GET'])
def get_dish_by_id(feedback_id):
    return feedback_controller.get_by_id(feedback_id)

@feedback_bp.route("/feedback", methods=['POST'])
def add_dish():
    return feedback_controller.create()

@feedback_bp.route("/feedback/<int:feedback_id>", methods=['PATCH'])
def update_actor(feedback_id):
    return feedback_controller.update(feedback_id)

@feedback_bp.route("/feedback/<int:feedback_id>", methods=['DELETE'])
def delete_dish(feedback_id):
    return feedback_controller.delete(feedback_id)