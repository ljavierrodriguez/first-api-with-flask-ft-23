from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default="active")
    
    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            "status": self.status
        }