# Задание №4
# 📌 Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('second.html')


@app.route('/next')
def next():
    return 'Привет, пользователь!'


@app.route('/post_img/', methods=['GET', 'POST'])
def post_img():
    context = {
        'task': 'Задание_2'
    }
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {escape(file_name)} загружен на сервер"
    return render_template('task_02.html', **context)


@app.route('/enter/', methods=['GET', 'POST'])
def enter():
    context = {
        'task': 'Задание3'
    }
    verification = {'login': '321',
                    'password': '123'
                    }
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == verification['login'] and password == verification['password']:
            return f"Вход {escape(login)} выполнен"
    return render_template('task4.html', **context)


@app.route('/letters/', methods=['GET', 'POST'])
def letters():
    context = {
        'task': 'Задание4'
    }
    if request.method == 'POST':
        text = request.form.get('text')
        length = len(text.split())
        return f"длина текста = {length} "
    return render_template('task4.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
