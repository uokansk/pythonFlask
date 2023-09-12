from flask import Flask
from lectures.lecture_03.models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Это 2 задача'


if __name__ == '__main__':
    app.run(debug=True)
