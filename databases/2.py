import sqlalchemy as db

sqlite_engine = db.create_engine('sqlite://sqlalchemy_sqlite.db')
postgresql_engine = db.create_engine('postgresql://test:teste@localhost:5432/postgresql.db')
mysql_engine = db.create_engine('mysql+mysqlconnector://test:test@localhost:3306/mysql.db')

sqlite_engine.tables_names()
postgresql_engine.tables_names()
mysql_engine.tables_names()
