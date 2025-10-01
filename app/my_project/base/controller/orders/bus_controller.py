from ..__init__ import BusService
from ..general_controller import GeneralController


class BusController(GeneralController):
    def __init__(self):
        super().__init__(BusService())
