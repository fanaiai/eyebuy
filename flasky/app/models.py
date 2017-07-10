from . import db
class Jiadian(db.Model):
	__tablename__='jiadian'
	id=db.Column(db.String(64), primary_key=True)
	name=db.Column(db.String(1000))
	url=db.Column(db.String(1000))
	price=db.Column(db.String(1000))
	images_url=db.Column(db.String(300))
	commentsnum=db.Column(db.String(10))


	def __repr__(self):
		return '%s :  %s' % (self.id,self.name)

class Taobaoitem(db.Model):
	__tablename__='taobaoitem'
	id=db.Column(db.String(64), primary_key=True)
	name=db.Column(db.String(1000))
	url=db.Column(db.String(1000))
	price=db.Column(db.String(1000))
	oriprice=db.Column(db.String(1000))
	comments=db.Column(db.Text)
