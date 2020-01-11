import sqlalchemy as db

engine = db.create_engine("mysql+mysqlconnector://root:foobar@localhost:3306/sqlalchemy_mysql")
connection = engine.connect()

query = 'SELECT * FROM tags'
result = engine.execute(query).first()

print(result)