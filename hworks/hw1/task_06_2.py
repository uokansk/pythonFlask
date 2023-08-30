# Задание №6
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/students/')
def students():
    _students = [{'family': 'Skill',
                 'name': 'Bill',
                  'age': 50,
                  'average_score': 5.0,
                  },
                 {'family': 'Vudi',
                  'name': 'Ailen',
                  'age': 40,
                  'average_score': 5.0,
                  },
                 {'family': 'Diter',
                  'name': 'Bolen',
                  'age': 30,
                  'average_score': 3.5,
                  },
                 {'family': 'Nomas',
                 'name': 'Fomas',
                  'age': 30,
                  'average_score': 3.0,
                  },
                 ]
    context = {'students': _students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
