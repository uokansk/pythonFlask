# Задание №1
# 📌 Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/next')
def next():
    return 'Привет, пользователь!'


# @app.route('/submit/', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello {name}!'
#     return render_template('forma_button.html')


if __name__ == '__main__':
    app.run(debug=True)
