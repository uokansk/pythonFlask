# Задание №9
# 📌 Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/shop/')
def shop():
    context = {'title': 'Магазин'}
    return render_template('shop.html', **context)


@app.route('/cloth/')
def cloth():
    head = {
        'type': 'Время года',
        'name': 'вид одежды',
        'price': 'цена',
    }
    cloth = [{'type': 'Зимняя',
               'name': 'Шапка',
               'price': 50,
               },
              {'type': 'Летняя',
               'name': 'Шубы',
               'price': 40,
               },
              {'type': 'Демисезонная',
               'name': 'Валенки',
               'price': 30,
               },
              ]
    title = {'title': 'Одежда'}
    return render_template('cloth.html', **head,  cloth=cloth, title=title)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    jacket = [{'header': 'Куртка 1',
              'short_text': 'Из искусственной чебурашки',
              'data_made': datetime.now().strftime(' %Y'),
              },
             {'header': 'Куртка 2',
              'short_text': 'Крашена кисточкой вручную',
              'data_made': datetime.now().strftime('%Y'),
              },
             {'header': 'Куртка 3',
              'short_text': 'Почти даром',
              'data_made': datetime.now().strftime('%Y'),
              },
             ]


    title = {'title': 'Куртка'}
    return render_template('jacket.html', title = title, jacket = jacket)


if __name__ == '__main__':
    app.run()