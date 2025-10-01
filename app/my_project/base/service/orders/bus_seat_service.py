from ..__init__ import BusSeat, BusSeatDAO
from ..genral_service import GeneralService
from my_project.database import db


class BusSeatService(GeneralService):
    def __init__(self):
        super().__init__(BusSeatDAO(), BusSeat)
        self.model = BusSeat

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
