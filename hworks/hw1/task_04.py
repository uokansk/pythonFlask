# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.


from flask import Flask

app = Flask(__name__)


@app.route('/text/<string:text>')
def len_text(text):
    return f'Длина строки = {len(text)}'


if __name__ == '__main__':
    app.run()
