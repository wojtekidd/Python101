import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///sqlalchemy2_csv.db')
engine.connect()
#
# with open("tags.csv", "r") as f:
#     tags_df = pd.read_csv(f)

# tags_df.to_sql('tags', con=engine)

print(engine.execute("select * from tags limit 10").fetchall())