import sqlalchemy as db

# mysql - tworzenie bazy
# engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306")
# engine.connect()
#
# engine.execute("CREATE DATABASE test_mysql")

# sqlite - tworzenie bazy
# engine = db.create_engine('sqlite:///new_sqlite.db')
# engine.connect()

# mysql - tworzenie tabeli
engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/test_mysql")
connection = engine.connect()

metadata = db.MetaData()

posts = db.Table('posts', metadata,
                 db.Column('Id', db.Integer, primary_key=True),
                 db.Column("Title", db.String(255)),
                 db.Column("ViewCount", db.Integer)
                 )


posts_two = db.Table(
    'posts_two', metadata,
    db.Column('Id', db.Integer, primary_key=True),
    db.Column('Title', db.String(255), nullable=False),
    db.Column('ViewCount', db.Integer, default=100),
    db.Column('isQuestion', db.Boolean, default=True)
)

metadata.create_all(engine)
# posts_two.create(engine)

stmt = db.insert(posts_two).values(Title="EFG")
result = connection.execute(stmt)
print(result.rowcount)

stmt = db.insert(posts_two)
values_list = [
    {'Title': "Pierwszy post"},
    {'Title': "Drugi post", "ViewCount": 200}
]
# Dlaczego 200 ?

result = connection.execute(stmt, values_list)
print(result.rowcount)