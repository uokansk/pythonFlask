# Задание №1
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!"

from flask import Flask

app = Flask(__name__)


@ app.route('/')
def home_work_t_1():
    return 'Hello, it is home work!!!'


if __name__ == '__main__':
    app.run()
