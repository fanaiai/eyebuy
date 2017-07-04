from flask import Flask ,request,make_response
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']=True
db=SQLAlchemy(app)

class Jiadian(db.Model):
	__tablename__='jiadian'
	id=db.Column(db.String(64), primary_key=True)
	name=db.Column(db.String(1000))
	url=db.Column(db.String(1000))
	price=db.Column(db.String(1000))

	def __repr__(self):
		return '%s :  %s' % (self.id,self.name)


def getResult(keyword):
	r=Jiadian.query.filter(Jiadian.name.swith(keyword)).all()
	print(r)

getResult('小猪')
@app.route("/",methods=['POST','GET'])
def hello():
	if request.method=='POST':
		keyword=request.form['keyword']
		print('____________%s' % keyword)
		return keyword
	else:
		# return 'get'
		return s

if __name__=='__main__':
	app.run()