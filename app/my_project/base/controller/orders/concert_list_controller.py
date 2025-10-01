from ..__init__ import ConcertListService
from ..general_controller import GeneralController


class ConcertListController(GeneralController):
    def __init__(self):
        super().__init__(ConcertListService())
