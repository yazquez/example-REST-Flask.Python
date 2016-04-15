import unittest
from api.lib.test_utils import BaseTestCase

class TestReadCompany(BaseTestCase):
    def test_read_company(self):
        resp = self.app.get('/companies/acme')
        assert b'New York' in resp.data

if __name__ == "__main__":
    unittest.main()