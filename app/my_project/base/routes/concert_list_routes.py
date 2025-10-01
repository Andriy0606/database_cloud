from flask import Blueprint
from ..controller.orders.concert_list_controller import ConcertListController

concert_list_bp = Blueprint("concert_list", __name__)
concert_list_controller = ConcertListController()


@concert_list_bp.route("/concert_list", methods=['GET'])
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
          application/json: [{"id": 1, "name": "Rock Fest", "location": "Kyiv"}]
    """
    return concert_list_controller.get_all()


@concert_list_bp.route("/concert_list/<int:concert_list_id>", methods=['GET'])
def get_concert_by_id(concert_list_id):
    """
    Отримати концерт за ID
    ---
    tags:
      - Concert List
    parameters:
      - name: concert_list_id
        in: path
        type: integer
        required: true
        description: ID концерту
    responses:
      200:
        description: Концерт знайдено
        examples:
          application/json: {"id": 1, "name": "Rock Fest", "location": "Kyiv"}
      404:
        description: Концерт не знайдено
    """
    return concert_list_controller.get_by_id(concert_list_id)


@concert_list_bp.route("/concert_list", methods=['POST'])
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
          properties:
            name:
              type: string
              example: "Rock Fest"
            location:
              type: string
              example: "Kyiv"
    responses:
      201:
        description: Концерт створено
    """
    return concert_list_controller.create()


@concert_list_bp.route("/concert_list/<int:concert_list_id>", methods=['PATCH'])
def update_concert(concert_list_id):
    """
    Оновити концерт за ID
    ---
    tags:
      - Concert List
    parameters:
      - name: concert_list_id
        in: path
        type: integer
        required: true
        description: ID концерту
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Updated Fest"
            location:
              type: string
              example: "Lviv"
    responses:
      200:
        description: Концерт оновлено
      404:
        description: Концерт не знайдено
    """
    return concert_list_controller.update(concert_list_id)


@concert_list_bp.route("/concert_list/<int:concert_list_id>", methods=['DELETE'])
def delete_concert(concert_list_id):
    """
    Видалити концерт за ID
    ---
    tags:
      - Concert List
    parameters:
      - name: concert_list_id
        in: path
        type: integer
        required: true
        description: ID концерту
    responses:
      200:
        description: Концерт видалено
      404:
        description: Концерт не знайдено
    """
    return concert_list_controller.delete(concert_list_id)
