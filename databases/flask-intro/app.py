from flask import Flask
from flask import render_template
# import sqlalchemy as db
# from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///airline.db"

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/hello")
def hello():
    return(render_template("hello.html"))

# session = sessionmaker()
# session.configure(bind=engine)
#
# my_session = session()