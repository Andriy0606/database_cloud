from my_project.database import db


class ConcertList(db.Model):
    __tablename__ = "concert_list"

    id = db.Column(db.String(10), primary_key=True)
    event_name = db.Column(db.String(45), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "event_name": self.event_name,
        }