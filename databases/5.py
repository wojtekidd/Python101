# 2. Deklaratywne API

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/sqlalchemy_mysql")
# engine.connect()

session = sessionmaker()
session.configure(bind=engine)
my_session = session()

Base = declarative_base()

class Tags(Base):
    __tablename__ = 'tags'
    Id = db.Column(db.Integer, primary_key=True)
    Count = db.Column(db.Integer)
    ExcerptPostId = db.Column(db.Integer)
    TagName = db.Column(db.String(255))
    WikiPostId = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.__class__.__name__} ID: {self.Id} - Name: {self.TagName}"

print(my_session.query(Tags).first())
print(type(my_session.query(Tags).first()))
print(my_session.query(Tags).first().Count)

# for each_tag in my_session.query(Tags):
#     print(each_tag)
#
# print(my_session.query(Tags))
#
# engine_echo = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/sqlalchemy_mysql", echo=True)
# connection_echo = engine_echo.connect()
# session_echo = sessionmaker(bind=engine_echo)()
#
# session_echo.query(Tags).first()

# Filtrowanie
print(my_session.query(Tags).filter_by(Count="11").all())
print(my_session.query(Tags).filter(Tags.Count=="12").all())

# like
print(my_session.query(Tags).filter(Tags.TagName.like('%matics%')).all())

# contains
print(my_session.query(Tags).filter(Tags.TagName.contains('matics')).all())
