from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///airline.db"


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/flights')
def hello():
    return render_template('flights.html')
