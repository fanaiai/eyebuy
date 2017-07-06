
def dec1():
	def wrap(fn):
		print('dec1')
		fn()
	return wrap

def dec2():
	def wrap(fn):
		print('dec2')
		fn()
	return wrap

@dec2()
@dec1()
def func1():
	print('func1')