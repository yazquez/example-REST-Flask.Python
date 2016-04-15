import unittest
from api.lib.test_utils import BaseTestCase

class TestReadCompanies(BaseTestCase):
    def test_read_company(self):
        resp = self.app.get('/companies')
        data = str(resp.data)
        assert("acme" in data and "pragma" in data)

if __name__ == "__main__":
    unittest.main()
