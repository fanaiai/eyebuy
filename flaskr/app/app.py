from flask import Flask,session ,request,make_response,current_app,jsonify
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']=True
db=SQLAlchemy(app)

# print(current_app.name)



class Jiadian(db.Model):
	__tablename__='jiadian'
	id=db.Column(db.String(64), primary_key=True)
	name=db.Column(db.String(1000))
	url=db.Column(db.String(1000))
	price=db.Column(db.String(1000))

	def __repr__(self):
		return '%s :  %s' % (self.id,self.name)


def getResult(keyword):
	r=Jiadian.query.filter(Jiadian.name.like("%"+keyword+"%")).all()
	rs=[]
	for i in r:
		rs.append({"name":i.name,"price":i.price})
	print(jsonify({"data":"rs"}))
	# return jsonify(rs)
getResult('小猪')
@app.route("/",methods=['POST','GET'])
def hello():
	if request.method=='POST':
		keyword=request.form['keyword']
		r=getResult(keyword)
		print('------%s' % r)
		
		return (r,200)
	else:
		# return 'get'
		print(app.app_context().name)
		return 's'

# if __name__=='__main__':
# 	app.run()