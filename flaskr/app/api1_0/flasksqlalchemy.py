from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']=True
db=SQLAlchemy(app)

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64))
	password=db.Column(db.String(64))
	email=db.Column(db.String(64))

	def __init__(self,username,password,email):
		self.username=username
		self.password=password
		self.email=email

	def __repr__(self):
		return '%s %s' % (self.id,self.username)

admin=User('haha','123','a@19')
db.session.add(admin)
db.session.commit()

user=User.query.all()
print(user)