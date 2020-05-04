import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
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
    # ToDO Write at least one test for each test for successful operation and for expected errors.

    def test_successful_connection(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_question_per_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_question_category_not_found_for_wrong_category(self):
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')
        self.assertEqual(data['error'], 404)

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['questions']), 10)
        self.assertTrue(data['total_questions'])

    def test_get_paginated_questions(self):
        res = self.client().get('/questions?page=2')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertLessEqual(len(data['questions']), 10)
        self.assertTrue(data['total_questions'])

    def test_post_questions(self):
        question = {
            'question': 'Who was first president of US?',
            'answer': 'Ibraham Lincon',
            'rating': 2,
            'category':2
        }
        res = self.client().post('/questions', json=question)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])

    def test_post_questions_bad_request_incomplete_data(self):
        res = self.client().post('/questions', json={'rating': 1})
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')
        self.assertEqual(data['error'], 400)

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/5')
    #     data = json.loads(res.data)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['deleted'])
    #     self.assertTrue(data['total_questions'])

    def test_search_questions(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'Tom'})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_quiz_questions(self):
        res = self.client().post('/quizzes', json={'quiz_category': {'id': 1}})
        data = json.loads(res.data)
        print(data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertTrue(len(data['question']))
        self.assertTrue(data['total_questions'])

    def test_quiz_questions_unprocessable(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')
        self.assertEqual(data['error'], 422)



# Make the tests conveniently executable
if __name__ == "__main__":
    print('a')
    unittest.main()