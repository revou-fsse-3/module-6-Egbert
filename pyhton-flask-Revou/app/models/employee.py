from app.utils.database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            "id" : self.id,
            "staff" : self.staff,
            "role" : self.role,
            "schedule" : self.schedule
        }