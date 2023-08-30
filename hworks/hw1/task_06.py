# Задание №6
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/studens/<string:family>/<string:name>/<string:age>/<float:average_score>')
def html_studens(family, name, age, average_score):
    context = {
        'family': family,
        'name': name,
        'age': age,
        'average_score': average_score
    }
    return render_template('studens.html', **context)


if __name__ == '__main__':
    app.run()
