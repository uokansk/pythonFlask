from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(80), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    authors = db.relationship('Author',
                              secondary='book_author',
                              backref='books',
                              lazy=True)

    def __repr__(self):
        return f'Student({self.name})'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'Autor({self.first_name} {self.last_name})'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
