# Задание №2
# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.
import random

from flask import Flask, render_template
from hworks.hw3.models_02 import db, BookAuthor, Book, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///liberty.db'
db.init_app(app)


@app.route('/')
def index():
    return 'семинар_3 задача_2'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-books")
def add_books():
    for i in range(1, 15):
        author = Author(first_name=f'first_name{i}',
                        last_name=f'last_name{i}',
                        )
        db.session.add(author)

    for i in range(1, 10):
        book = Book(name=f'name{i}',
                    year=i+2000,
                    count=i)
        db.session.add(book)

    for i in range(0, 15):
        book_author = BookAuthor(book_id=random.randint(1, 9),
                                 author_id=random.randint(1, 14),
                                 )
        db.session.add(book_author)
    db.session.commit()
    print('Готово!')


@app.route('/books/', methods=['GET'])
def all_books():
    book = Book.query.all()
    context = {'book': book}
    return render_template('books.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
