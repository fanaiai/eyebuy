from . import api

@api.route('',methods=['GET','POST'])
def index():
	return '什么东西啊blueprint'