# ORM - classical mapping
import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapper

engine = db.create_engine('mysql+mysqlconnector://root:foobar@localhost:3306/sqlalchemy_mysql')
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
        self.count = Count
        self.excerptPostId = ExcerptPostId
        self.tagName = TagName
        self.wikiPostId = WikiPostId


tags_mapper = Mapper(Tags, tags)

larger_tags = tags.select(Tags.Count > 1000)
result = engine.execute(larger_tags).fetchall()
print(result)
