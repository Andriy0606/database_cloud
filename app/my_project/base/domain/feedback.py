from my_project.database import db

class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.String(10), db.ForeignKey("concert_list.id"), primary_key=True)
    feedback = db.Column(db.String(200), nullable=True)


    def to_dict(self):
        return {
            "id": self.id,
            "feedback": self.feedback,
        }
