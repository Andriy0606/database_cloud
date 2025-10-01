from flask import Blueprint
from ..controller.orders.bus_seat_controller import BusSeatController

bus_seat_bp = Blueprint("bus_seat", __name__)
bus_seat_controller = BusSeatController()


@bus_seat_bp.route("/bus_seat", methods=['GET'])
def get_bus_seats():
    """
    Отримати список місць в автобусах
    ---
    tags:
      - Bus Seat
    responses:
      200:
        description: Список місць
        examples:
          application/json: [{"id": 1, "bus_id": 2, "seat_number": 12, "is_reserved": false}]
    """
    return bus_seat_controller.get_all()


@bus_seat_bp.route("/bus_seat/<int:bus_seat_id>", methods=['GET'])
def get_bus_seat_by_id(bus_seat_id):
    """
    Отримати місце за ID
    ---
    tags:
      - Bus Seat
    parameters:
      - name: bus_seat_id
        in: path
        type: integer
        required: true
        description: ID місця
    responses:
      200:
        description: Місце знайдено
        examples:
          application/json: {"id": 1, "bus_id": 2, "seat_number": 12, "is_reserved": false}
      404:
        description: Місце не знайдено
    """
    return bus_seat_controller.get_by_id(bus_seat_id)


@bus_seat_bp.route("/bus_seat", methods=['POST'])
def add_bus_seat():
    """
    Додати місце в автобусі
    ---
    tags:
      - Bus Seat
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            bus_id:
              type: integer
              example: 2
            seat_number:
              type: integer
              example: 15
            is_reserved:
              type: boolean
              example: false
    responses:
      201:
        description: Місце додано
    """
    return bus_seat_controller.create()


@bus_seat_bp.route("/bus_seat/<int:bus_seat_id>", methods=['PATCH'])
def update_bus_seat(bus_seat_id):
    """
    Оновити місце
    ---
    tags:
      - Bus Seat
    parameters:
      - name: bus_seat_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            seat_number:
              type: integer
              example: 20
            is_reserved:
              type: boolean
              example: true
    responses:
      200:
        description: Місце оновлено
      404:
        description: Місце не знайдено
    """
    return bus_seat_controller.update(bus_seat_id)


@bus_seat_bp.route("/bus_seat/<int:bus_seat_id>", methods=['DELETE'])
def delete_bus_seat(bus_seat_id):
    """
    Видалити місце
    ---
    tags:
      - Bus Seat
    parameters:
      - name: bus_seat_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Місце видалено
      404:
        description: Місце не знайдено
    """
    return bus_seat_controller.delete(bus_seat_id)
