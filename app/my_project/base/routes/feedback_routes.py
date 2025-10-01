from flask import Blueprint
from ..controller.orders.feedback_controller import FeedbackController

feedback_bp = Blueprint("feedback", __name__)
feedback_controller = FeedbackController()


@feedback_bp.route("/feedback", methods=["GET"])
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
          application/json:
            - { "id": "EVT001", "feedback": "Дуже класно!" }
            - { "id": "EVT002", "feedback": "Непогано" }
    """
    return feedback_controller.get_all()


@feedback_bp.route("/feedback/<string:feedback_id>", methods=["GET"])
def get_feedback_by_id(feedback_id):
    """
    Отримати відгук за ID концерту (FK на concert_list.id)
    ---
    tags:
      - Feedback
    parameters:
      - name: feedback_id
        in: path
        type: string
        required: true
        description: ID концерту (наприклад, 'EVT003')
    responses:
      200:
        description: Відгук знайдено
        examples:
          application/json: { "id": "EVT003", "feedback": "Було супер" }
      404:
        description: Відгук не знайдено
    """
    return feedback_controller.get_by_id(feedback_id)


@feedback_bp.route("/feedback", methods=["POST"])
def add_feedback():
    """
    Додати/створити відгук для концерту
    ---
    tags:
      - Feedback
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [id, feedback]
          properties:
            id:
              type: string
              description: FK на concert_list.id (PRIMARY KEY feedback)
              example: "EVT003"
            feedback:
              type: string
              maxLength: 200
              example: "Все сподобалось!"
    responses:
      201:
        description: Відгук додано
      404:
        description: Концерту з таким id не існує (FK)
      409:
        description: Конфлікт PK (для цього концерту відгук уже існує)
    """
    return feedback_controller.create()


@feedback_bp.route("/feedback/<string:feedback_id>", methods=["PATCH"])
def update_feedback(feedback_id):
    """
    Оновити відгук для концерту (PK = concert_list.id)
    ---
    tags:
      - Feedback
    parameters:
      - name: feedback_id
        in: path
        type: string
        required: true
        description: ID концерту
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            feedback:
              type: string
              maxLength: 200
              example: "Оновлений коментар"
    responses:
      200:
        description: Відгук оновлено
      404:
        description: Відгук/концерт не знайдено
    """
    return feedback_controller.update(feedback_id)


@feedback_bp.route("/feedback/<string:feedback_id>", methods=["DELETE"])
def delete_feedback(feedback_id):
    """
    Видалити відгук (PK = concert_list.id)
    ---
    tags:
      - Feedback
    parameters:
      - name: feedback_id
        in: path
        type: string
        required: true
        description: ID концерту
    responses:
      200:
        description: Відгук видалено
      404:
        description: Відгук не знайдено
    """
    return feedback_controller.delete(feedback_id)
