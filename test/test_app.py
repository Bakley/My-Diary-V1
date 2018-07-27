<<<<<<< HEAD:test/test_app.py
from app.route import app
=======
from app.manage import app
>>>>>>> 41a78b3814663e85a6cfaa3da35e601cd09ae270:test_app.py

import unittest
import json

class BasicTestCase(unittest.TestCase):
    """main"""
    
    def test_index(self):
        """Initial test: Ensure flask was set up correctly."""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        """Define the test variable and set up a temporary DB"""
        self.url_route1 = '/mydiary/api/v1/entries'
        self.url_route2 = '/mydiary/api/v1/entries/1'
        self.entry = {
            "id": 1,
            "Date": "Monday",
            "Title": "I am learning all about TDD",
            "Body": "Its sounds simple in theory wait untill you actually try it out.." 
        }
      

    def test_api_can_get_all_diary_entries(self):
        """Test if the API can fetch all the Enries (Methods = GET)"""
        tester = app.test_client(self)
        response = tester.get(self.url_route1, content_type='html/text')
        self.assertEqual(response.status_code, 200)
        response = tester.get(self.url_route2, content_type='html/text')
        self.assertEqual(response.status_code, 404)


    def test_api_can_create_a_new_diary_entry(self):
        """Test if the API can create an Entry (Methods = POST)"""
        pass

    def test_api_can_Update_a_diary_entries(self):
        """Test if the API can update an Entry (Methods = PUT)"""
        pass

    def test_api_can_delete_a_diary_entries(self):
        """Test if the API can delete an Entry (Methods = DELETE)"""
        tester = app.test_client(self)
        response = tester.delete(self.url_route2)
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()