from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    password = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'User({self.firstname}, {self.lastname}, {self.email}, {self.password})'
