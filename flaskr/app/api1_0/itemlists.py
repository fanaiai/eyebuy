from flask import Flask,session ,request,make_response,current_app,jsonify
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
from app import db

class Jiadian(db.Model):
	__tablename__='jiadian'
	id=db.Column(db.String(64), primary_key=True)
	name=db.Column(db.String(1000))
	url=db.Column(db.String(1000))
	price=db.Column(db.String(1000))

	def __repr__(self):
		return '%s :  %s' % (self.id,self.name)


def getResult(keyword):
	r=Jiadian.query.filter(Jiadian.name.endswith(keyword)).all()
	return r
	
@api.route('/itemlists')
def get_lists():
	keyword=request.form['keyword']
	re=
