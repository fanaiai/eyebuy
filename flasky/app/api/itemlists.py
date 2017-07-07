from . import api
from ..models import Jiadian,Taobaoitem
from .. import db
from flask import request
import json

def getResult(keyword,source):
	jd,tb,jdcount,tbcount=[],[],0,0
	for i in source:
		if(i==""):
			jd=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).slice(0,10).all()
			jdcount=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).count()
			tb=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).slice(0,10).all()
			tbcount=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).count()
		elif(i=="1"):
			jd=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).limit(10).all()
			jdcount=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).count()
		elif(i=="2"):
			tb=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).limit(10).all()
			tbcount=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).count()
	count=jdcount+tbcount
	rs=[]
	for i in jd:
		rs.append({"name":i.name,"price":i.price if i.price!='无' else i.oriprice,"url":i.url,"comments":i.commentsnum})
	for i in tb:
		comments=0
		c=json.loads(i.comments.replace("\'","\""))
		if(type(c) is int):
			comments=i.comments
		else:
			comments=c.get("total")
		rs.append({"name":i.name,"price":i.price if i.price!='无' else i.oriprice,"url":i.url,"comments":comments})
	res={"data":rs,"count":count}
	return json.dumps(res)

@api.route('/getList/',methods=['POST','GET'])
def getList():
	if(request.method=='POST'):
		keyword=request.form['keyword']
		source=request.form['source'].split(',')
		r=getResult(keyword,source)
		return r
	else:
		return getResult('小猪')
