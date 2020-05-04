import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db
from config import bearer_tokens


writer_auth_bearer_token = {
    'Authorization': bearer_tokens['writer']
}

editor_auth_bearer_token = {
    'Authorization': bearer_tokens['editor']
}

class NewsAggregationTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		"""Define test variables and initialize app."""
		self.app = create_app()
		self.client = self.app.test_client
		self.database_name = "newsapp_test"
		self.database_path = "postgres://{}/{}".format('postgres:12345678@localhost:5432', self.database_name)
		setup_db(self.app, self.database_path)

		# binds the app to the current context
		with self.app.app_context():
			self.db = SQLAlchemy()
			self.db.init_app(self.app)
			# create all tables
			self.db.create_all()

	def tearDown(self):
		"""Executed after reach test"""
		pass

	def test_successful_connection(self):
		res = self.client().get('/all_news')
		self.assertEqual(res.status_code, 200)

	def test_get_categories(self):
		res = self.client().get('/categories')
		data = json.loads(res.data)

		self.assertEqual(data['success'], True)
		self.assertTrue(data['categories'])
		self.assertTrue(len(data['categories']))

	def test_get_all_news(self):
		res = self.client().get('/all_news')
		data = json.loads(res.data)

		self.assertEqual(data['success'], True)
		self.assertTrue(data['news'])
		self.assertLessEqual(len(data['news']), 5)
		self.assertTrue(data['total_news'])

	def test_all_news_page_not_found_for_wrong_category(self):
		res = self.client().get('/all_news/100')
		data = json.loads(res.data)

		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Not Found')
		self.assertEqual(data['error'], 404)

	def test_get_one_news(self):
		res = self.client().get('/news/2')
		data = json.loads(res.data)

		self.assertEqual(data['success'], True)
		self.assertTrue(data['news'])

	def test_post_news(self):
		news = {
			'headline':    'This is a test news',
			'description': 'This is description of test news',
			'img_url':     'https://example.com/img1.png',
			'category':    2
		}
		res = self.client().post('/news', json=news, headers=writer_auth_bearer_token)
		data = json.loads(res.data)

		self.assertEqual(data['success'], True)
		self.assertTrue(data['created'])

	def test_post_news_bad_request_incomplete_data(self):
		res = self.client().post('/news', json={'category': 1}, headers=writer_auth_bearer_token)
		data = json.loads(res.data)

		self.assertEqual(data['success'], False)
		self.assertEqual(data['message'], 'Bad Request')
		self.assertEqual(data['error'], 400)
	#
	# def test_delete_news(self):
	# 	res = self.client().delete('/news/1', headers=editor_auth_bearer_token)
	# 	data = json.loads(res.data)
	# 	self.assertEqual(data['success'], True)
	# 	self.assertTrue(data['deleted'])

	def test_update_news(self):
		news = {
			'headline':    'This is an updated news'
		}
		res = self.client().patch('/news/2', json=news, headers=writer_auth_bearer_token)
		data = json.loads(res.data)
		self.assertEqual(data['success'], True)
		self.assertTrue(data['edited'])


# Make the tests conveniently executable
if __name__ == "__main__":
	print('a')
	unittest.main()
