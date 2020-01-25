import sqlalchemy as db

engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/sqlalchemy_mysql")
engine.connect()

query = """SELECT OwnerUserId,
SUM(AnswerCount) AS 'TotalAnswers',
SUM(ViewCount) As 'TotalViews'
FROM posts
WHERE owneruserid is not NULL
GROUP BY OwnerUserId
ORDER BY 'TotalAnswers' DESC
LIMIT 10;"""

result = engine.execute(query).fetchall()
print(result)