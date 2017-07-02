from flask import Flask ,request,make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']=True
db=SQLAlchemy(app)

class Jiadian(db.Model):
	__tablename__='jiadian'
	id=db.Column(db.String(64), primary_key=True)
	name=db.Column(db.String(64))

	def __repr__(self):
		return '%s :  %s' % (self.id,self.name)

# jiadian=Jiadian()
# db.create_all()
re=Jiadian.query.all()
r=re
print(r)
@app.route("/",methods=['POST','GET'])
def hello():
	if request.method=='POST':
		return "Hello World!"
	else:
		return 'get'
		# return "".join(Jiadian.query.filter_by(id='3133829').all())

if __name__=='__main__':
	app.run()