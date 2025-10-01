from ..__init__ import BusSeatService
from ..general_controller import GeneralController


class BusSeatController(GeneralController):
    def __init__(self):
        super().__init__(BusSeatService())
