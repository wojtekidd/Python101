from flask import Flask
from flask import render_template
from models import Flights, db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///airline.db"
db.init_app(app)

@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/flights')
def flights():
    """List all flights"""
    flights = Flights.query.all()
    return render_template('flights.html', flights=flights)
