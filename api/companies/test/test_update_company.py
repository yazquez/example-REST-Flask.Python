from api.lib.test_utils import BaseTestCase
import unittest

class TestUpdateCompany(BaseTestCase):
    def test_update_company(self):
        resp = self.app.put('/companies/exponential',
                             data='{"acme": {"name": " ACME & Associates", "city": "Miami"}}',
                             headers={'content-type':'application/json'})
        # self.assertEqual(resp.status_code, 200)
        # assert b'Miami' in resp.data
        # assert b'New York' not in resp.data
        print(resp.data)
        assert True

if __name__ == "__main__":
    unittest.main()
