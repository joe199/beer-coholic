from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
     __tablename__ = 'DataBase'
     # this field will identify uniquely any user in the database
     # more info here -> http://www.w3schools.com/sql/sql_primarykey.asp
     id = Column(Integer, primary_key=True)
     username = Column(String)
     tagid = Column(String)
     name = Column(String)

     def __repr__(self):
        return "<User(username='%s', tagid='%s', name='%s')>" % (
                             self.username, self.tagid, self.name)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
from sqlalchemy import create_engine
path_to_db = "usuaris.db"
engine = create_engine('sqlite:///' + path_to_db)
Base.metadata.create_all(engine)
