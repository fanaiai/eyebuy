from flask import Flask
from .config import config
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy
import pymysql

db=SQLAlchemy()

def create_app(config_name):
	app=Flask(__name__)
	CORS(app, supports_credentials=True)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)

	from .api import api
	app.register_blueprint(api,url_prefix='/api')
	return app

