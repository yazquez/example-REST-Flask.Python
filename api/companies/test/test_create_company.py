from api.lib.test_utils import BaseTestCase
import unittest
class TestCreateCompany(BaseTestCase):
    def test_create_company(self):
        resp = self.app.post('/companies',
                             data='{"alliorg": {"name": "Alliorg. Inc.", "city": "Toronto"}}',
                             headers={'content-type':'application/json'})
        self.assertEqual(resp.status_code, 201)
        assert b'boeing' not in resp.data
        assert b'alliorg' in resp.data
if __name__ == "__main__":
    unittest.main()