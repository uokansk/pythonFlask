from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'Привет task_04, {name.capitalize()}!'


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'


@app.route('/number/<float:num> <float:num1>/')
def set_number(num, num1):
    print(type(num))
    return f'Передано число {num} {num1}'


if __name__ == '__main__':
    app.run()
