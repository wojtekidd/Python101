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
        return f"{self.__class__.__name__ } Id: {self.Id} - Name: {self.DisplayName}"

# filter
print(my_session.query(Users).filter_by(DisplayName="Community").all())

# like
for item in my_session.query(Users.DisplayName).filter(Users.DisplayName.like("%Cot%")).all():
    print(item)

# func
from sqlalchemy import func

# func.sum
print(my_session.query(func.sum(Users.UpVotes)).scalar())

# difference, limit
print(my_session.query(Users.DisplayName,
                       Users.UpVotes - Users.DownVotes,
                       Users.UpVotes,
                       Users.DownVotes).limit(10).all())

# etykietowanie
print(my_session.query(Users.DisplayName,
                       (Users.UpVotes - Users.DownVotes).label("vote_difference"),
                       Users.UpVotes,
                       Users.DownVotes).limit(10).all())

# rzutowanie
print(my_session.query(Users.DisplayName,
                       db.cast((Users.UpVotes - Users.DownVotes), db.Numeric(12, 2)).label("vote_difference"),
                       Users.UpVotes,
                       Users.DownVotes).limit(10).all())

# sortowanie rosnąco (domyślnie)
print(my_session.query(Users.DisplayName,
                       db.cast((Users.UpVotes - Users.DownVotes), db.Numeric(12, 2)).label("vote_difference"),
                       Users.UpVotes,
                       Users.DownVotes).order_by('vote_difference').limit(10).all())

# sortowanie malejąco (desc)
print(my_session.query(Users.DisplayName,
                       db.cast((Users.UpVotes - Users.DownVotes), db.Numeric(12, 2)).label("vote_difference"),
                       Users.UpVotes,
                       Users.DownVotes).order_by(db.desc('vote_difference')).limit(10).all())


processed_query = my_session.query(Users.Id,
                       (Users.UpVotes - Users.DownVotes).label("vote_difference"),
                       Users.UpVotes,
                       Users.DownVotes).order_by(Users.Id).all()

# x, y1, y2 = [], [], []
# import matplotlib.pyplot as plt
# for item in processed_query:
#     x.append(item[0])
#     y1.append(item[1])
#     y2.append(item[2])
#
# plt.scatter(x, y2, label="UpVotes")
# plt.plot(x, y1, 'r', label="Vote difference", linewidth=1)
# plt.legend()
#
# plt.show()
#

