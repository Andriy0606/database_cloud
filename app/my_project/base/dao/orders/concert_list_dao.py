from my_project.base.dao.general_dao import GeneralDAO


class ConcertListDAO(GeneralDAO):
    from my_project.base.dao.__init__ import ConcertList
    def __init__(self):
        super().__init__(self.ConcertList)