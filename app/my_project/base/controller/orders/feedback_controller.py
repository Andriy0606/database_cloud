from ..__init__ import FeedbackService
from ..general_controller import GeneralController


class FeedbackController(GeneralController):
    def __init__(self):
        super().__init__(FeedbackService())
