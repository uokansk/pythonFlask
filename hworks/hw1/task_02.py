# Задание №2
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, it is home work!!!'


@app.route('/about/')
def about():
    return 'Hello, about!!!'


@app.route('/contact/')
def contact():
    return 'Hello, contact!!!'


if __name__ == '__main__':
    app.run()
