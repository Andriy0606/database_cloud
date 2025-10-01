from flask import Blueprint
from ..controller.orders.bus_controller import BusController

bus_bp = Blueprint("bus", __name__)
bus_controller = BusController()


@bus_bp.route("/bus", methods=['GET'])
def get_bus():
    """
    Отримати список автобусів
    ---
    tags:
      - Bus
    responses:
      200:
        description: Список автобусів
        examples:
          application/json: [{"id": 1, "model": "Neoplan", "seats": 50}]
    """
    return bus_controller.get_all()


@bus_bp.route("/bus/<int:bus_id>", methods=['GET'])
def get_bus_by_id(bus_id):
    """
    Отримати автобус за ID
    ---
    tags:
      - Bus
    parameters:
      - name: bus_id
        in: path
        type: integer
        required: true
        description: ID автобуса
    responses:
      200:
        description: Автобус знайдено
        examples:
          application/json: {"id": 1, "model": "Neoplan", "seats": 50}
      404:
        description: Автобус не знайдено
    """
    return bus_controller.get_by_id(bus_id)


@bus_bp.route("/bus", methods=['POST'])
def add_bus():
    """
    Додати автобус
    ---
    tags:
      - Bus
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              example: "Mercedes Sprinter"
            seats:
              type: integer
              example: 20
    responses:
      201:
        description: Автобус додано
    """
    return bus_controller.create()


@bus_bp.route("/bus/<int:bus_id>", methods=['PATCH'])
def update_bus(bus_id):
    """
    Оновити автобус
    ---
    tags:
      - Bus
    parameters:
      - name: bus_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              example: "Renault Master"
            seats:
              type: integer
              example: 30
    responses:
      200:
        description: Автобус оновлено
      404:
        description: Автобус не знайдено
    """
    return bus_controller.update(bus_id)


@bus_bp.route("/bus/<int:bus_id>", methods=['DELETE'])
def delete_bus(bus_id):
    """
    Видалити автобус
    ---
    tags:
      - Bus
    parameters:
      - name: bus_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Автобус видалено
      404:
        description: Автобус не знайдено
    """
    return bus_controller.delete(bus_id)
