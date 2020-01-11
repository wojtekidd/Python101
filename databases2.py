import sqlalchemy as db

#sqlite_engine = db.create_engine('sqlite://sqlalchemy_sqlite.db')
#postgresql_engine = db.create_engine('postgresql://test:test@localhost:5432/postgresql.db')
engine = db.create_engine('mysql+mysqlconnector://root:foobar@localhost:3306/sqlalchemy_mysql')
engine.connect()

query = """SELECT OwnerUserId,
SUM(AnswerCount) AS 'TotalAnswers',
SUM(ViewCount) AS 'TotalViews'
FROM posts
WHERE OwnerUserID is not NULL
GROUP BY OwnerUserId
ORDER BY 'TotalAnswers' DESC
LIMIT 10;"""

result = engine.execute(query).fetchall()

print(result)

