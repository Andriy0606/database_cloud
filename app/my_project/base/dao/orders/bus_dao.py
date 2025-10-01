from my_project.base.dao.general_dao import GeneralDAO
from my_project.base.dao.__init__ import Bus

class BusDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Bus)
