from test.model.test_dao import TestDao

class TestService:
	def test_get(self):
		test_dao = TestDao()
		test_result = test_dao.test_get()
		return test_result
