from flask import jsonify

class TestDao:
	def test_get(self):
		return jsonify({'message':'pong'}), 200
