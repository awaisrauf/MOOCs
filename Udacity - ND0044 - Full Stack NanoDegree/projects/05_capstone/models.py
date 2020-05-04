import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=None):
	db.app = app
	app.config["SQLALCHEMY_DATABASE_URI"] = database_path
	db.init_app(app)
	#db.create_all()


'''
News
'''


class News(db.Model):
	__tablename__ = 'news'

	id = Column(Integer, primary_key=True)
	headline = Column(String)
	description = Column(String)
	img_url = Column(String)
	category = Column(Integer)

	def __init__(self, headline, description, img_url, category_id):
		self.headline = headline
		self.answer = description
		self.img_url = img_url
		self.category = category_id

	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
			'id':          self.id,
			'headline':    self.headline,
			'description': self.description,
			'img_url':     self.img_url,
			'category':    self.category
		}


'''
Category

'''


class Category(db.Model):
	__tablename__ = 'categories'

	id = Column(Integer, primary_key=True)
	type = Column(String)

	def __init__(self, type):
		self.type = type

	def format(self):
		return {
			'id':   self.id,
			'type': self.type
		}
