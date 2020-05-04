import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, News, Category
from flask_cors import CORS
from auth0 import AuthError, requires_auth


NEWS_PER_PAGE = 5


def paginate_news(request, selection):
	page = request.args.get('page', 1, type=int)
	start = (page - 1) * NEWS_PER_PAGE
	end = start + NEWS_PER_PAGE

	newsz = [news.format() for news in selection]
	current_newsz = newsz[start: end]
	return current_newsz


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__)
	app.config.from_object('config')
	setup_db(app, app.config["SQLALCHEMY_DATABASE_URI"])
	CORS(app)

	@app.after_request
	def after_request(response):
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
		response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
		return response

	@app.route('/', methods=["GET"])
	def main_msessage():
		return jsonify({
			'success':    True,
			'message': "You have come to right news source"
		})

	@app.route('/categories', methods=["GET"])
	def get_categories():
		categories = Category.query.all()
		if len(categories) == 0:
			abort(404)
		try:
			cats = {cat.id: cat.type for cat in categories}
			return jsonify({
				'success': True,
				'categories': cats
			})
		except:
			abort(422)

	@app.route('/all_news', methods=["GET"])
	def get_all_news():
		news = News.query.all()
		if len(news) == 0:
			abort(404)
		try:
			news = paginate_news(request, news)
			return jsonify({
				'success': True,
				'news': news,
				'total_news': len(news)
			})
		except:
			abort(422)

	@app.route('/news/<int:news_id>', methods=["GET"])
	def get_one_news(news_id):
		news = News.query.filter(News.id == news_id).all()
		if len(news)==0:
			abort(404)
		try:
			news = paginate_news(request, news)
			return jsonify({
				'success': True,
				'news':    news
			})
		except:
			abort(422)

	@app.route('/news/<int:news_id>', methods=['DELETE'])
	@requires_auth('delete:news')
	def delete_news(payload, news_id):
		news = News.query.filter(News.id == news_id).one_or_none()
		if news is None:
			abort(422)

		try:
			news.delete()
			return jsonify({
				'success':         True,
				'deleted':          news_id,
				'total_news': len(News.query.all())
			})
		except:
			abort(400)

	@app.route('/news', methods=['POST'])
	@requires_auth('post:news')
	def add_news(payload):
		data = request.get_json()

		headline = data.get('headline', None)
		description = data.get('description', None)
		category_id = data.get('category', None)
		img_url = data.get('img_url', None)
		if headline is None or category_id is None:
			abort(400)
		try:
			news = News(headline=headline, description=description, category_id=category_id, img_url=img_url)
			news.insert()

			selection = News.query.order_by(News.id).all()
			current_news = paginate_news(request, selection)
			return jsonify({
				'success': True,
				'created': news.id,
				'news': current_news,
				'total_news': len(News.query.all())
			})
		except:
			abort(422)

	@app.route('/news/<int:news_id>', methods=['PATCH'])
	@requires_auth('edit:news')
	def update_news(payload, news_id):
		news = News.query.filter(News.id == news_id).one_or_none()
		if news is None:
			abort(422)

		data = request.get_json()

		headline = data.get('headline', None)
		description = data.get('description', None)
		category_id = data.get('category_id', None)
		img_url = data.get('img_url', None)
		try:
			if headline is not None:
				news.headline = headline
			if description is not None:
				news.description = description
			if category_id is not None:
				news.category_id = category_id
			if img_url is not None:
				news.img_url = img_url
			news.update()
			return jsonify({
				'success':         True,
				'edited':          news_id,
				'total_news': len(News.query.all())
			})
		except:
			abort(400)



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

	@app.errorhandler(AuthError)
	def unauthorized(e):
		return jsonify({
			"success": False,
			"error":   e.status_code,
			"message": list(e.error)[0]
		})


	return app


app = create_app()

if __name__ == '__main__':
	APP.run(host='127.0.0.1', port=5000, debug=True)
