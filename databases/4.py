# 1. ORM - Klasyczne mapowanie

import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper

engine = db.create_engine("mysql+mysqlconnector://jgrynczewski:1234@localhost:3306/sqlalchemy_mysql")
engine.connect()

metadata = MetaData()
tags = db.Table('Tags', metadata,
                db.Column('Id', db.Integer, primary_key=True),
                db.Column('Count', db.Integer),
                db.Column('ExcerptPostId', db.Integer),
                db.Column('TagName', db.String(255)),
                db.Column('WikiPostId', db.Integer)
                )

class Tags:
    def __init__(self, Count, ExcerptPostId, TagName, WikiPostId):
        self.Count = Count
        self.excerptPostId = ExcerptPostId
        self.tagName = TagName
        self.wikiPostId = WikiPostId

tags_mapper = mapper(Tags, tags)

larger_tags = tags.select(Tags.Count > 1000)

result = engine.execute(larger_tags).fetchall()
print(result)
print(type(result))
