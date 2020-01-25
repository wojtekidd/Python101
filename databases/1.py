import pandas as pd
import sqlalchemy as db

engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/sqlalchemy_mysql")
connection = engine.connect()

query = 'SELECT * FROM posts'
# result = engine.execute(query).fetchall()
# print(result)

posts_df = pd.read_sql_query(query, engine)
# print(type(posts_df))
# print(posts_df)
print(posts_df.columns)
# print(posts_df.dtypes)
print(posts_df[['ViewCount', 'AnswerCount']])
print(posts_df[['ViewCount', 'AnswerCount']].max())
print(posts_df[['ViewCount', 'AnswerCount']].min())
print(posts_df[['ViewCount', 'AnswerCount']].min())
print(posts_df[['ViewCount', 'AnswerCount']].describe())
print(posts_df[['ViewCount', 'AnswerCount']].dropna()[:50])

import matplotlib.pyplot as plt

x = posts_df['AnswerCount'].dropna()[:200]
y = posts_df['ViewCount'].dropna()[:200]

import numpy as np
colors = np.random.rand(200)

plt.scatter(x, y, c=colors)
plt.title('Posts: Views vs. Answers')
plt.xlabel("Answers")
plt.ylabel("Views")
plt.show()
