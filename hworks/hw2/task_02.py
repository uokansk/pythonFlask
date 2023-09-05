# Задание №2
# 📌 Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.
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


# @app.route('/submit/', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello {name}!'
#     return render_template('forma_button.html')


if __name__ == '__main__':
    app.run(debug=True)
