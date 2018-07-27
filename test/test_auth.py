import unittest
import json
#  import the models
from app.createdb import connect_to_db

from app import create_app

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        conn = connect_to_db('testing')
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        cur.execute("""DROP TABLE IF EXISTS users CASCADE""" )
        cur.execute("""DROP TABLE IF EXISTS entries CASCADE""" )

        self.create_users_table(cur)
        self.create_entries_table(cur)
        
        self.app = create_app('testing')
        with self.app.app_context():
            from app.models.usermodel import User, Entry
        self.client = self.app.test_client()

        self.entry_model = Entry
        self.user_model = User
       
        self.user_data = {
                    "username":"koin", 
                    "email":"koin@hotmail.com",
                    "password":"password123"
                    }
        self.entry_data = {
                    "title": "Freaky friday",
                    "description": "Fun fun fun fun fun fun"
                    }

        self.user1 = User(
            username='testuser',
            email='testuser@email.com',
            password='password')

        self.entry1 = Entry(
            title='I saved a dog',
            description='The dog was cute',
            user_id=1)

        self.test_user = User(
            username='koin',
            email='koin@hotmail.com',
            password='password123')

    def test_user_registration(self):
        """Test  if the user registration works correctly"""
        response = self.client.post('/auth/register', data=self.user_data)
        # The data is returned in json format
        result = json.loads(response.data.decode)  
        # assert if the response contains a success message and a  201 status code
        self.assertEqual(result['message'], "You have successfully registered, please proceed"])
        self.assertEqual(response.status_code, 201)

    def test_already_registered_user(self):
        """Test that a user cannot register twice"""]
        response = self.client().post('/auth/register', data=self.user_data)
        # assert first response == status code  201
        self.assertEqual(response.status_code, 201)

        second_response =  self.client().post('/auth/register', data=self.user_data)
        # assert the second response is a status code 202
        self.assertEqual(response.status_code, 202)

        # Get the results of returned in json format
        result = json.load.(second_response.data.decode())
        self.assertEqual(result['message'], "User already exists"])

    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


    