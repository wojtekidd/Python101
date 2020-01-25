import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/sqlalchemy_mysql")

session = sessionmaker()
session.configure(bind=engine)
my_session = session()

Base = declarative_base()

class Users(Base):
    __tablename__= 'users'
    Id = db.Column(db.Integer, primary_key=True)
    AboutMe = db.Column(db.String(255))
    AccountId = db.Column(db.Integer)
    CreationDate = db.Column(db.DateTime)
    DisplayName = db.Column(db.String(255))
    DownVotes = db.Column(db.Integer)
    LastAccessDate = db.Column(db.DateTime)
    Location = db.Column(db.String(255))
    ProfileImageUrl = db.Column(db.String(255))
    Reputation = db.Column(db.Integer)
    UpVotes = db.Column(db.Integer)
    Views = db.Column(db.Integer)
    WebsiteUrl = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.__class__.__name__} - Name: {self.DisplayName}"

class Posts(Base):
    __tablename__ = 'posts'
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer, default=1000)
    OwnerUserId = db.Column(db.Integer)

    __table_args__ = {'extend_existing': True}
    ResponseId = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.__class__.__name__}- Title {self.Title}"

# Niejawny join
result = my_session.query(Users, Posts).filter(Users.Id == Posts.OwnerUserId).all()

for item in result[:5]:
    print(item)

# Jawny join
print(my_session.query(Users, Posts).join(Posts, Users.Id == Posts.OwnerUserId).first())

# Tablica hierarchiczne

from sqlalchemy.orm import aliased
Responses = aliased(Posts)
print(Responses)


