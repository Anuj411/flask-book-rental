from wsgiref.validate import validator
from extensions import db

class user(db.Model):
    __tablename__ = 'user_model'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<user {self.full_name}>'
