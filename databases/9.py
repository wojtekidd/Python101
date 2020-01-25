import sqlalchemy as db

engine = db.create_engine('sqlite:///new_sqlite.db')
connection = engine.connect()

metadata = db.MetaData()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))


class Post(Base):
        __tablename__ = 'post'
        Id = db.Column(db.Integer, primary_key=True)
        Title = db.Column(db.String(255), nullable=False)
        ViewCount = db.Column(db.Integer, default=100)
        Question = db.Column(db.Boolean, default=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
my_session = session()

Ewa = User(Name="Ewa")
Adam = User(Name="Adam")

my_session.add(Ewa)
my_session.add(Adam)

print(my_session.new)
my_session.commit()

one_post = Post(Title="Pierwsz wpis", ViewCount=200)
one_answer = Post(Title="Pierwsza odpowiedz", Question=False)

# posts = []
# for item in range(100):
#     posts.append(Post(Title=f"Wpis numer {item}"))

# my_session.add_all(posts)
# my_session.add_all([one_post, one_answer])
# my_session.commit()

# print(engine.execute("select * from post").fetchall())

# 1. Update za pomocą surowego sql
# print(engine.execute("select ViewCount from post where Id=1").fetchone())
# engine.execute("update post set ViewCount=150 where Id=1")
#
# print(engine.execute("select ViewCount from post where Id=1").fetchone())


#. Update za pomocą orm
# query = db.update(Post).where(Post.Id==1).values(ViewCount=20)
# result = connection.execute(query)
#
# post_query = my_session.query(Post).filter(Post.Id==1).one()
# print(post_query.ViewCount)

# Update wiele wierszy
query = db.update(Post).values(ViewCount = Post.ViewCount+50)
result = connection.execute(query)
print(my_session.query(Post.ViewCount).all())

# 3. Update przez zmianę pola
# my_post = my_session.query(Post).filter(Post.Id == 1).one()
# my_post.ViewCount = 1000 # Dlaczego "asd" działa?Z
# my_session.commit()

# Delete przez orm
# first_post = my_session.query(Post).first()
# print(first_post.Id)
#
# my_session.delete(first_post)
#
# print(my_session.query(Post.Id).first())
# my_session.commit()

#2. delete
# my_session.query(Post).filter(Post.Id > 120).delete()
# my_session.commit()

# Usunięcie tabeli

metadata.reflect(bind=engine)
print(metadata.tables.keys())

# 1 Usuwanie tabeli
Base.metadata.drop_all(bind=engine, tables=[Post.__table__])

# 2. Usuwanie tabeli
User.__table__.drop(engine)