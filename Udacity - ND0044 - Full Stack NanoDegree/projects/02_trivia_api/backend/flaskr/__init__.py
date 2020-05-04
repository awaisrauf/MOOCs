import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from  sqlalchemy.sql.expression import func, select
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
	page = request.args.get('page', 1, type=int)
	start = (page - 1)*QUESTIONS_PER_PAGE
	end = start + QUESTIONS_PER_PAGE

	questions = [question.format() for question in selection]
	current_questions = questions[start: end]
	return current_questions


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__)
	setup_db(app)

	# Done: TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
	CORS(app, resources={r"/api/*": {"origins": "*"}})

	# Done: TODO: Use the after_request decorator to set Access-Control-Allow
	@app.after_request
	def after_request(response):
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
		response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
		return response

	# Done: TODO:  Create an endpoint to handle GET requests for all available categories.
	@app.route('/categories', methods=["GET"])
	def get_categories():
		categories = Category.query.all()
		try:
			if len(categories) == 0:
				abort(404)
			else:
				cats = {cat.id: cat.type for cat in categories}
				return jsonify({
					'success': True,
					'categories': cats
				})
		except:
			abort(422)

	@app.route('/categories/<int:category_id>/questions', methods=["GET"])
	def get_each_category_questions(category_id):
		questions = Question.query.filter(Question.category == category_id).all()

		if len(questions) == 0:
			abort(404)
		try:

			current_questions = paginate_questions(request, questions)
			return jsonify({
				'success': True,
				'questions': current_questions,
				'current_category': category_id,
				'total_questions': len(questions)
			})
		except:
			abort(422)

	# Done: TODO: Create an endpoint to handle GET requests for questions,
	'''
	including pagination (every 10 questions). 
	This endpoint should return a list of questions, 
	number of total questions, current category, categories. 
	
	TEST: At this point, when you start the application
	you should see questions and categories generated,
	ten questions per page and pagination at the bottom of the screen for three pages.
	Clicking on the page numbers should update the questions. 
	'''
	@app.route('/questions', methods=['GET'])
	def get_questions():
		questions = Question.query.all()
		categories = Category.query.all()
		if len(questions) == 0:
			abort(404)
		try:
			selected_questions = paginate_questions(request, questions)
			cats = {cat.id: cat.type for cat in categories}
			return jsonify({
				'success': True,
				'questions': selected_questions,
				'current_category': None,
				'categories': cats,
				'total_questions': len(questions)
			})
		except:
			abort(422)

	# Done: TODO: Create an endpoint to DELETE question using a question ID.
	'''
	TEST: When you click the trash icon next to a question, the question will be removed.
	This removal will persist in the database and when you refresh the page. 
	'''
	@app.route('/questions/<int:question_id>', methods=['DELETE'])
	def delete_question(question_id):
		question = Question.query.filter(Question.id == question_id).one_or_none()
		if question is None:
			abort(422)

		try:
			question.delete()
			return jsonify({
				'success':         True,
				'deleted':          question_id,
				'total_questions': len(Question.query.all())
			})
		except:
			abort(400)

	# Done: TODO: Create an endpoint to POST a new question,
	'''
	Create an endpoint to POST a new question, 
	which will require the question and answer text, 
	category, and difficulty score.
  
	TEST: When you submit a question on the "Add" tab, 
	the form will clear and the question will appear at the end of the last page
	of the questions list in the "List" tab.  
	'''
	@app.route('/questions', methods=['POST'])
	def add_question():
		data = request.get_json()

		question = data.get('question', None)
		answer = data.get('answer', None)
		category = data.get('category', None)
		difficulty = data.get('difficulty', None)
		if question is None or answer is None:
			abort(400)
		try:
			question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
			question.insert()

			selection = Question.query.order_by(Question.id).all()
			current_questions = paginate_questions(request, selection)
			return jsonify({
				'success': True,
				'created': question.id,
				'questions': current_questions,
				'total_questions': len(Question.query.all())
			})
		except:
			abort(422)

	# Done TODO: Create a POST endpoint to get questions based on a search term.
	'''
	It should return any questions for whom the search term 
	is a substring of the question. 
	TEST: Search by any phrase. The questions list will update to include 
	only question that include that string within their question. 
	Try using the word "title" to start. 
	'''
	@app.route('/questions/search', methods=['POST'])
	def search_questions():
		data = request.get_json()
		search_term = data.get('searchTerm', None)
		questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
		print(data)
		if len(questions) == 0:
			abort(404)
		try:
			return jsonify({
				'success': True,
				'questions': [q.format() for q in questions],
				'total_questions': len(Question.query.all()),
				'current_category': None
			})
		except:
			abort(422)

	# Done: TODO: Create a POST endpoint to get questions to play the quiz.
	'''
	This endpoint should take category and previous question parameters 
	and return a random questions within the given category, 
	if provided, and that is not one of the previous questions. 
  
	TEST: In the "Play" tab, after a user selects "All" or a category,
	one question at a time is displayed, the user is allowed to answer
	and shown whether they were correct or not. 
	'''
	@app.route('/quizzes', methods=['POST'])
	def get_question_for_quiz():
		data = request.get_json()
		category = data.get('quiz_category', None)
		previous_questions = data.get('previous_questions', None)

		try:
			# assign random category if no category is submitted
			if category['id'] == 0:
				category['id'] = random.randint(1, 5)
            # get a random question while making sure that it is not one of perevious ones.    
			if previous_questions:
				question = Question.query.filter(Question.category == category['id']).order_by(func.random()).first()
				while question.id in previous_questions:
					question = Question.query.filter(Question.category == category['id']).order_by(
						func.random()).first()
			else:
				question = Question.query.filter(Question.category == category['id']).order_by(func.random()).first()

			return jsonify({
				'success':         True,
				'question':       question.format(),
				'total_questions': len(Question.query.all())

			})
		except:
			abort(422)

	# Done TODO: Create error handlers for all expected errors  including 404 and 422.
	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
			'success': False,
			'error': 404,
			'message': 'Not Found'
		})

	@app.errorhandler(422)
	def unprocessable(error):
		return jsonify({
			'success': False,
			'error':   422,
			'message': 'Unprocessable'
		})

	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({
			'success': False,
			'error':   400,
			'message': 'Bad Request'
		})

	return app
