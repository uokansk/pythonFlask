# Задание
# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля
# "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные
# должны сохраняться в базе данных, а пароль должен быть зашифрован.


from flask import Flask, request, render_template
from hworks.hw3.task3.models import db, User
from flask_wtf import CSRFProtect
from hworks.hw3.task3.forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usersbase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'семинар_3 домашняя работа'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        users = User(firstname=firstname, lastname=lastname, email=email, password=password)
        db.session.add(users)
        db.session.commit()
        return f'User add'

    return render_template('register.html', form=form)


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    users = User.query.all()
    return f'{list(users)}'
