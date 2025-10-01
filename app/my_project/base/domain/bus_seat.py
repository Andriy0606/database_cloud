from my_project.database import db

class BusSeat(db.Model):
    __tablename__ = "bus_seat"

    bus_no = db.Column(db.Integer, db.ForeignKey("bus.bus_no"), primary_key=True)
    seat_no = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Enum("Yes", "No"), nullable=True)

    def to_dict(self):
        return {
            "bus_no": self.bus_no,
            "seat_no": self.seat_no,
            "is_available": self.is_available,
        }
