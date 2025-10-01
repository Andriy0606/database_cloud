from flask import Blueprint
from ..controller.orders.concert_list_controller import ConcertListController

concert_list_bp = Blueprint("concert_list", __name__)
concert_list_controller = ConcertListController()


@concert_list_bp.route("/concert_list", methods=["GET"])
def get_concert_list():
    """
    Отримати список концертів
    ---
    tags:
      - Concert List
    responses:
      200:
        description: Список концертів
        examples:
          application/json:
            - { "id": "EVT001", "event_name": "Rock Fest" }
            - { "id": "EVT002", "event_name": "Jazz Night" }
    """
    return concert_list_controller.get_all()


@concert_list_bp.route("/concert_list/<string:concert_list_id>", methods=["GET"])
def get_concert_by_id(concert_list_id):
    """
    Отримати концерт за ID
    ---
    tags:
      - Concert List
    parameters:
      - name: concert_list_id
        in: path
        type: string
        required: true
        description: ID концерту (до 10 символів)
    responses:
      200:
        description: Концерт знайдено
        examples:
          application/json: { "id": "EVT001", "event_name": "Rock Fest" }
      404:
        description: Концерт не знайдено
    """
    return concert_list_controller.get_by_id(concert_list_id)


@concert_list_bp.route("/concert_list", methods=["POST"])
def add_concert():
    """
    Додати новий концерт
    ---
    tags:
      - Concert List
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [event_name]      # id можна передавати, якщо у тебе він не генерується на боці сервера
          properties:
            id:
              type: string
              maxLength: 10
              example: "EVT003"
              description: "Опційно: якщо PK не генерується автоматично"
            event_name:
              type: string
              example: "Sympho Night"
    responses:
      201:
        description: Концерт створено
        examples:
          application/json: { "id": "EVT003", "event_name": "Sympho Night" }
      400:
        description: Некоректні дані
      409:
        description: Назва вже існує (unique constraint)
    """
    return concert_list_controller.create()


@concert_list_bp.route("/concert_list/<string:concert_list_id>", methods=["PATCH"])
def update_concert(concert_list_id):
    """
    Оновити концерт за ID
    ---
    tags:
      - Concert List
    parameters:
      - name: concert_list_id
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
            event_name:
              type: string
              example: "Updated Fest"
    responses:
      200:
        description: Концерт оновлено
        examples:
          application/json: { "id": "EVT001", "event_name": "Updated Fest" }
      404:
        description: Концерт не знайдено
    """
    return concert_list_controller.update(concert_list_id)


@concert_list_bp.route("/concert_list/<string:concert_list_id>", methods=["DELETE"])
def delete_concert(concert_list_id):
    """
    Видалити концерт за ID
    ---
    tags:
      - Concert List
    parameters:
      - name: concert_list_id
        in: path
        type: string
        required: true
        description: ID концерту
    responses:
      200:
        description: Концерт видалено
        examples:
          application/json: { "message": "deleted", "id": "EVT001" }
      404:
        description: Концерт не знайдено
    """
    return concert_list_controller.delete(concert_list_id)
