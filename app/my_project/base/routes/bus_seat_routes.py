from flask import Blueprint
from ..controller.orders.bus_seat_controller import BusSeatController

bus_seat_bp = Blueprint("bus_seat", __name__)
bus_seat_controller = BusSeatController()


@bus_seat_bp.route("/bus_seat", methods=["GET"])
def get_bus_seats():
    """
    Отримати всі місця (по всіх автобусах)
    ---
    tags:
      - Bus Seat
    responses:
      200:
        description: Список місць
        examples:
          application/json:
            - { "bus_no": 101, "seat_no": 1, "is_available": "Yes" }
            - { "bus_no": 101, "seat_no": 2, "is_available": "No" }
    """
    return bus_seat_controller.get_all()


@bus_seat_bp.route("/bus_seat/<int:bus_no>", methods=["GET"])
def get_bus_seat_by_id(bus_no):
    """
    Отримати всі місця для конкретного автобуса (PK = bus_no)
    ---
    tags:
      - Bus Seat
    parameters:
      - name: bus_no
        in: path
        type: integer
        required: true
        description: Номер автобуса (FK на bus.bus_no)
    responses:
      200:
        description: Список місць для вказаного автобуса
        examples:
          application/json:
            - { "bus_no": 101, "seat_no": 1, "is_available": "Yes" }
            - { "bus_no": 101, "seat_no": 2, "is_available": "No" }
      404:
        description: Місця/автобус не знайдено
    """
    return bus_seat_controller.get_by_id(bus_no)


@bus_seat_bp.route("/bus_seat", methods=["POST"])
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
          required: [bus_no, seat_no]
          properties:
            bus_no:
              type: integer
              description: FK на bus.bus_no (а також PK цього запису)
              example: 101
            seat_no:
              type: integer
              description: Номер місця в автобусі
              example: 12
            is_available:
              type: string
              enum: ["Yes", "No"]
              description: Доступність місця
              example: "Yes"
    responses:
      201:
        description: Місце додано
      404:
        description: Автобуса з таким bus_no не існує
      409:
        description: Конфлікт унікальності/PK (bus_no вже існує)
    """
    return bus_seat_controller.create()


@bus_seat_bp.route("/bus_seat/<int:bus_no>", methods=["PATCH"])
def update_bus_seat(bus_no):
    """
    Оновити місця для автобуса (за PK = bus_no)
    ---
    tags:
      - Bus Seat
    parameters:
      - name: bus_no
        in: path
        type: integer
        required: true
        description: Номер автобуса (PK/FK)
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            seat_no:
              type: integer
              description: Новий/оновлений номер місця (якщо логіка контролера дозволяє)
              example: 20
            is_available:
              type: string
              enum: ["Yes", "No"]
              example: "No"
    responses:
      200:
        description: Оновлено
      404:
        description: Не знайдено
      409:
        description: Конфлікт унікальності
    """
    return bus_seat_controller.update(bus_no)


@bus_seat_bp.route("/bus_seat/<int:bus_no>", methods=["DELETE"])
def delete_bus_seat(bus_no):
    """
    Видалити місця за автобусом (PK = bus_no)
    ---
    tags:
      - Bus Seat
    parameters:
      - name: bus_no
        in: path
        type: integer
        required: true
        description: Номер автобуса (PK/FK)
    responses:
      200:
        description: Видалено
      404:
        description: Не знайдено
    """
    return bus_seat_controller.delete(bus_no)
