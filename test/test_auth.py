import unittest
import json

# from app import  models.models

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client
        # This is the user test json data with a predefined email and password
        self.user_data = {
            'email': 'test@example.com',
            'password': 'test_password'
        }

        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_user_registration(self):
        """Test  if the user registration works correctly"""
        response = self.client().post('/auth/register', data=self.user_data)
        # The data is returned in json format
        result = json.load.(response.data.decode())  
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

    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


    