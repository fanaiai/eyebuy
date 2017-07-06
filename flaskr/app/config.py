import os
print(os.path.dirname)
# basedir = os.path.abspath(os.path.dirname="__file__")

class Config():
	SECRET_KEY= os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
	FLASKY_MAIL_SENDER='Flasky Admin <flasky@example.com>'
	FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG= True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
'mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4'

config={
	'development':DevelopmentConfig,
	'default':DevelopmentConfig
}