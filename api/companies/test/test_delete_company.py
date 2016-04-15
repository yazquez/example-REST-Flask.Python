from api.lib.test_utils import BaseTestCase
import unittest


class TestDeleteCompany(BaseTestCase):
    def test_delete_company(self):
        resp = self.app.delete('/companies/acme',
                               headers={'content-type':'application/json'})
        # self.assertEqual(resp.status_code, 200)
        assert b'acme' in resp.data

if __name__ == "__main__":
    unittest.main()
