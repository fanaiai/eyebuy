from . import api
from ..models import Jiadian,Taobaoitem,Yihaoitem
from .. import db
from flask import request
import json
import math

def getResult(keyword,source,page):
	jd,tb,jdcount,tbcount=[],[],0,0
	pagel=(page-1)*10;
	pager=page*10
	for i in source:
		if(i==""):
			jd=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).slice(pagel,pager).all()
			jdcount=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).count()
			yihao=Yihaoitem.query.filter(Yihaoitem.name.like('%'+keyword+'%')).slice(pagel,pager).all()
			yihaocount=Yihaoitem.query.filter(Yihaoitem.name.like('%'+keyword+'%')).count()
			tb=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).slice(pagel,pager).all()
			tbcount=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).count()
		elif(i=="1"):
			jd=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).slice(pagel,pager).all()
			jdcount=Jiadian.query.filter(Jiadian.name.like('%'+keyword+'%')).count()
		elif(i=="2"):
			tb=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).slice(pagel,pager).all()
			tbcount=Taobaoitem.query.filter(Taobaoitem.name.like('%'+keyword+'%')).count()
		elif(i=="3"):
			yihao=Yihaoitem.query.filter(Yihaoitem.name.like('%'+keyword+'%')).slice(pagel,pager).all()
			yihaocount=Yihaoitem.query.filter(Yihaoitem.name.like('%'+keyword+'%')).count()
	count=jdcount+tbcount+yihaocount
	rs=[]
	for i in jd:
		rs.append({"name":i.name,"price":i.price if i.price!='无' else i.oriprice,"url":i.url,"comments":i.commentsnum,"images_url":i.images_url})
	for i in yihao:
		rs.append({"name":i.name,"price":i.price if i.price!='无' else i.oriprice,"url":i.url,"comments":i.commentsnum,"images_url":i.images_url})
	for i in tb:
		comments=0
		c=json.loads(i.comments.replace("\'","\""))
		if(type(c) is int):
			comments=i.comments
		else:
			comments=c.get("total")
		rs.append({"name":i.name,"price":i.price if i.price!='无' else i.oriprice,"url":i.url,"comments":comments,"images_url":"img/jd1.jpg"})
	res={"data":rs,"count":count,"totalpage":math.ceil(count/10)}
	return json.dumps(res)

@api.route('/getList/',methods=['POST','GET'])
def getList():
	if(request.method=='POST'):
		keyword=request.form['keyword']
		page=int(request.form['page'])
		source=request.form['source'].split(',')
		r=getResult(keyword,source,page)
		return r
	else:
		return getResult('小猪')
