from flask import Blueprint
from ..controller.orders.feedback_controller import FeedbackController

feedback_bp = Blueprint("feedback", __name__)
feedback_controller = FeedbackController()


@feedback_bp.route("/feedback", methods=['GET'])
def get_feedback():
    """
    Отримати всі відгуки
    ---
    tags:
      - Feedback
    responses:
      200:
        description: Список відгуків
        examples:
          application/json: [{"id": 1, "user": "Ivan", "comment": "Дуже класно!", "rating": 5}]
    """
    return feedback_controller.get_all()


@feedback_bp.route("/feedback/<int:feedback_id>", methods=['GET'])
def get_feedback_by_id(feedback_id):
    """
    Отримати відгук за ID
    ---
    tags:
      - Feedback
    parameters:
      - name: feedback_id
        in: path
        type: integer
        required: true
        description: ID відгуку
    responses:
      200:
        description: Відгук знайдено
        examples:
          application/json: {"id": 1, "user": "Ivan", "comment": "Дуже класно!", "rating": 5}
      404:
        description: Відгук не знайдено
    """
    return feedback_controller.get_by_id(feedback_id)


@feedback_bp.route("/feedback", methods=['POST'])
def add_feedback():
    """
    Додати відгук
    ---
    tags:
      - Feedback
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user:
              type: string
              example: "Ivan"
            comment:
              type: string
              example: "Все сподобалось!"
            rating:
              type: integer
              example: 5
    responses:
      201:
        description: Відгук додано
    """
    return feedback_controller.create()


@feedback_bp.route("/feedback/<int:feedback_id>", methods=['PATCH'])
def update_feedback(feedback_id):
    """
    Оновити відгук
    ---
    tags:
      - Feedback
    parameters:
      - name: feedback_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            comment:
              type: string
              example: "Оновлений коментар"
            rating:
              type: integer
              example: 4
    responses:
      200:
        description: Відгук оновлено
      404:
        description: Відгук не знайдено
    """
    return feedback_controller.update(feedback_id)


@feedback_bp.route("/feedback/<int:feedback_id>", methods=['DELETE'])
def delete_feedback(feedback_id):
    """
    Видалити відгук
    ---
    tags:
      - Feedback
    parameters:
      - name: feedback_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Відгук видалено
      404:
        description: Відгук не знайдено
    """
    return feedback_controller.delete(feedback_id)
