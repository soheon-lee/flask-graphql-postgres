import os

from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from test.view.test_view import TestView

def create_app():
	app = Flask(__name__)
	app.config.from_object(os.environ['APP_SETTINGS'])
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db = SQLAlchemy(app)

	CORS(app)

	app.register_blueprint(TestView.test_app)

	return app
