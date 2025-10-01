# app/my_project/base/routes/bus_routes.py
from flask import Blueprint
from ..controller.orders.bus_controller import BusController

bus_bp = Blueprint("bus", __name__)
bus_controller = BusController()


@bus_bp.route("/bus", methods=["GET"])
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
          application/json:
            - { "id": "EVT001", "bus_no": 101 }
            - { "id": "EVT002", "bus_no": 202 }
    """
    return bus_controller.get_all()


@bus_bp.route("/bus/<string:bus_id>", methods=["GET"])
def get_bus_by_id(bus_id):
    """
    Отримати автобус за ID (FK на concert_list.id)
    ---
    tags:
      - Bus
    parameters:
      - name: bus_id
        in: path
        type: string
        required: true
        description: ID концерту (concert_list.id), до якого прив'язаний автобус
    responses:
      200:
        description: Автобус знайдено
        examples:
          application/json: { "id": "EVT001", "bus_no": 101 }
      404:
        description: Автобус не знайдено
    """
    return bus_controller.get_by_id(bus_id)


@bus_bp.route("/bus", methods=["POST"])
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
          required: [id, bus_no]
          properties:
            id:
              type: string
              description: FK на concert_list.id (наприклад, "EVT003")
              example: "EVT003"
            bus_no:
              type: integer
              description: Унікальний номер автобуса
              example: 303
    responses:
      201:
        description: Автобус додано
      400:
        description: Некоректні дані
      404:
        description: Концерту з таким id не існує
      409:
        description: Конфлікт унікальності (bus_no або PK уже існує)
    """
    return bus_controller.create()


@bus_bp.route("/bus/<string:bus_id>", methods=["PATCH"])
def update_bus(bus_id):
    """
    Оновити автобус (міняємо лише bus_no)
    ---
    tags:
      - Bus
    parameters:
      - name: bus_id
        in: path
        type: string
        required: true
        description: Поточний PK/FG (concert_list.id), за яким шукаємо запис
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            bus_no:
              type: integer
              description: Новий унікальний номер автобуса
              example: 404
    responses:
      200:
        description: Автобус оновлено
      404:
        description: Автобус не знайдено
      409:
        description: Конфлікт унікальності (такий bus_no вже існує)
    """
    return bus_controller.update(bus_id)


@bus_bp.route("/bus/<string:bus_id>", methods=["DELETE"])
def delete_bus(bus_id):
    """
    Видалити автобус
    ---
    tags:
      - Bus
    parameters:
      - name: bus_id
        in: path
        type: string
        required: true
        description: PK/FG (concert_list.id)
    responses:
      200:
        description: Автобус видалено
      404:
        description: Автобус не знайдено
    """
    return bus_controller.delete(bus_id)
