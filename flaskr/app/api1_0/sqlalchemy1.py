from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer
import pymysql

engine=create_engine('mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4',echo=True)
print(engine)

DBSession=sessionmaker(bind=engine)


Base=declarative_base()

class User(Base):
	__tablename__='users'

	id=Column(Integer,primary_key=True)
	username=Column(String(64),nullable=False,index=True)
	password=Column(String(64),nullable=False)
	email=Column(String(64),nullable=False)

	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__,self.id)

session=DBSession()
# Base.metadata.create_all(engine)
new_user=User(username='fyy1',password='fyy',email='5@com.com')

session.add(new_user)
print(session.new)
session.commit()
user=session.query(User).filter(User.id==5).count()
print(user)
for u in user:
	print('%s -----   %s' % (u,u.password))
session.close()

