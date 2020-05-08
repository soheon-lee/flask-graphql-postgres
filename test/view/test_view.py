import json

from flask import request, Blueprint, jsonify
from test.service.test_service import TestService

class TestView:
	test_app = Blueprint('test_app', __name__, url_prefix='/ping')

	@test_app.route('', methods=['GET'], endpoint='test_get')
	def test_get():
		test_service = TestService()
		test_result = test_service.test_get()
		return test_result
	
