import os

class Config():
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG=True
	SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:11111111@localhost:3306/python?charset=utf8mb4'

config={
	'development':DevelopmentConfig,
	'default':DevelopmentConfig
}