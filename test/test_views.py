import unittest
import psycopg2
import json

from app.config_database import config
from app.models.usermodel import User, Entries
from app import app

class TestBasicAuth(unittest.TestCase):
    """ We test the models and views"""

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.user = User(username='Barclay', password='password', email = "name@test.com")
        self.user2 = User(username='Koin', password='passwor2', email = "test@name.com")
        self.user3 = User(username='postgre', password='database',email = "post@gres.com")


    def sign_up_user(self, user):
        """Helper method that issues the request to sign up a user"""
        req_data = {'username': user.username,
                    'password': user.password_hash,
                    'email': user.email}
        response = self.client.post('/mydiary/api/v1/user/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(req_data))
        return response

    def login_user(self, user):
        """Helper method that issues the request to login a user"""
        req_data = {'username': user.username,
                    'password': user.password_hash}
        response = self.client.post('/mydiary/api/v1/user/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(req_data))
        return response

    def login_signup(self, user):
        """Helper method to login and sign up a user"""
        resp = self.sign_up_user(user)
        self.assertEqual(201, resp.status_code)
        resp = self.login_user(user)
        self.assertEqual(200, resp.status_code)
        data = json.loads(str(resp.data.decode()))
        self.assertIn('access_token', data)

        return data['access_token']

    def test_signup(self):
        """Test if the user sign up is working correctly"""
        response = self.sign_up_user(self.user)
        self.assertEqual(response.status_code, 201)
        

    def test_login(self):
        """"Test if the user login is working correctly"""
        response = self.login_user(self.user)
        self.assertEqual(response.status_code, 201)

    def test_user_login_twice(self):
        response = self.login_user(self.user2)
        self.assertEqual(response.status_code, 201)
        response = self.login_user(self.user2)
        self.assertIn(self.user2, self.user2)

    def test_welcome_message(self):
        """Test the welcome message"""
