from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Тестовый сайт. Главная страница'


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)