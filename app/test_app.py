import unittest
from requests import get, post

from app.index import *


class TestApp(unittest.TestCase):

    def test_home(self):
        responce = get("http://localhost:5000/")
        status = responce.status_code

        self.assertEqual(status, 200)

    def test_login(self):
        no_valid_user = {'username': 'user10', 'password': 'adwdwdwdw'}
        valid_user = {'username': 'test', 'password': 'password'}

        responce = post('http://localhost:5000/login/', no_valid_user)
        status = responce.status_code
        self.assertEqual(status, 401)

        responce = post('http://localhost:5000/login/', valid_user)
        status = responce.status_code
        self.assertNotEqual(status, 200)

if __name__ == '__main__':
    unittest.main()