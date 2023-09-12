from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!'
    # return '42'


if __name__ == '__main__':
    app.run()


# Для запуска через консоль  PS C:\Users\kapa-\PycharmProjects\pythonFlask>
# flask --app .\lecture_01\main.py run