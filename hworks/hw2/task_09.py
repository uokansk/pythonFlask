# Задание №9
# 📌 Создать страницу, на которой будет форма для ввода имени и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными пользователя
# 📌 Также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from pathlib import PurePath, Path
from flask import Flask, request, render_template, make_response, redirect
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('forma_hw.html')


@app.route('/enter/', methods=['POST'])
def enter():
    name = request.form['name']
    email = request.form['email']

    response = make_response(redirect('/welcome'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response


@app.route('/welcome/')
def welcome():
    name = request.cookies.get('user_name')
    if name:
        return render_template('welcome.html', name=name)
    return redirect('/')


@app.route('/output/')
def output():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
