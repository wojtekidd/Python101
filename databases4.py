#ORM - declarative API

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('mysql+mysqlconnector://root:foobar@localhost:3306/sqlalchemy_mysql')
connection = engine.connect()

session = sessionmaker()
session.configure(bind=engine)
my_session = session()

Base = declarative_base()

class Tags(Base):
    __tablename__ = 'Tags'
    Id = db.Column(db.Integer, primary_key=True)
    Count = db.Column(db.Integer)
    ExcerptPostId = db.Column(db.Integer)
    TagName = db.Column(db.String(255))
    WikiPostId = db.Column(db.Integer)


    def __repr__(self):
        return f"{self.__class__.__name__} ID: {self.Id} - Name: {self.TagName}"

print(my_session.query(Tags).all())
print(type(my_session.query(Tags).all()))