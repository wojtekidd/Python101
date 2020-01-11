import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt

engine = db.create_engine('mysql+mysqlconnector://root:foobar@localhost:3306/sqlalchemy_mysql')
connection = engine.connect()

query = 'SELECT ViewCount, AnswerCount FROM posts where ViewCount is not NULL'

# result = engine.execute(query).fetchall()
# print(result)

posts_df = pd.read_sql_query(query, engine)
# print(posts_df)
# print('---')
# print(posts_df.columns)
# print('---')
# print(posts_df.dtypes)
# print('---')
# print(posts_df.head())
# print('---')
# print(posts_df[['ViewCount', 'AnswerCount']].max())
# print('---')
# print(posts_df[['ViewCount', 'AnswerCount']].describe())
# print('---')

x = posts_df['AnswerCount']
y = posts_df['ViewCount']
plt.scatter(x, y)
plt.ylim([0, 20])
plt.xlabel('Answers')
plt.ylabel('Views')
plt.title('Posts: Views vs. Answers')
plt.show()