# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумм

from flask import Flask

app = Flask(__name__)


@app.route('/summa/<float:num_a>/<float:num_b>/')
def sum_number(num_a, num_b):
    return f'{num_a} + {num_b} = {num_a + num_b}'


if __name__ == '__main__':
    app.run()
