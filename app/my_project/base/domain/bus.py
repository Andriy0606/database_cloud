from my_project.database import db


class Bus(db.Model):
    __tablename__ = "bus"

    id = db.Column(db.String(10), db.ForeignKey("concert_list.id"), primary_key=True)
    bus_no = db.Column(db.Integer, nullable=False, unique=True)

    # Відношення до ConcertList
    concert = db.relationship("ConcertList", backref=db.backref("buses", lazy=True))

    # Відношення до BusSeat
    seats = db.relationship("BusSeat", backref=db.backref("bus", lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "bus_no": self.bus_no,
        }
