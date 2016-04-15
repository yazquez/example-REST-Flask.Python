"""Testing utilities"""
import api
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """Run before test"""
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()
    def tearDown(self):
        """Run after test"""
        pass

