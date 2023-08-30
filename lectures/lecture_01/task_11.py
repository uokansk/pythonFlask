from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    # return render_template('main.html', **context)
    return render_template('new_main.html', **context)



@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    # return render_template('data.html', **context)
    return render_template('new_data.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
