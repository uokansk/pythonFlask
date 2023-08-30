# Задание №7
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через контекст.
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/news/')
def news():
    _news = [{'header': 'Курс евро превысил 105 рублей',
              'short_text': 'Рубль усиливает снижение к евро, который на фоне укрепления на форексе '
                            'превысил 105 рублей впервые с 16 августа, следует из данных Московской биржи.',
              'data_news': datetime.now().strftime('%d, %B, %Y'),
              },
             {'header': 'Расследовать крушение',
              'short_text': 'Россия не будет расследовать крушение самолета Пригожина по правилам ИКАО',
              'data_news': datetime.now().strftime('%d, %B, %Y'),
              },
             {'header': 'На дне Тихого океана',
              'short_text': 'На дне Тихого океана нашли «шарики» внеземного происхождения',
              'data_news': datetime.now().strftime('%d, %B, %Y'),
              },
             ]

    context = {'news': _news}
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run()
