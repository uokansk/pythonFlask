# Задание №1
# 📌 Создать базу данных для хранения информации о студентах университета.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# 📌 В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# 📌 Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.
import random

from flask import Flask, render_template
from hworks.hw3.models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///univerdatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'семинар_3 задача_1'


@app.route('/students/', methods=['GET'])
def all_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_student():
    for i in range(1, 4):
        faculty = Faculty(faculty_name=f'faculty{i}')
        db.session.add(faculty)
    for i in range(0, 10):
        student = Student(first_name=f'first_name{i}',
                          last_name=f'last_name{i}',
                          age=random.randint(18, 21),
                          gender=random.choice(['male', 'female']),
                          group=random.randint(1, 5),
                          faculty_id=random.randint(1, 3)
                          )
        db.session.add(student)
    db.session.commit()
    print('Готово!')


if __name__ == '__main__':
    app.run(debug=True)
