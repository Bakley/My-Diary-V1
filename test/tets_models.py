import unittest
import os

from app.models.createdb import connect_to_db
from app.models.createdb_helper import Database
class BasicDatabaseTest(unittest.TestCase):
    """Test out db and models"""

    def setUp(self):
        connector = "dbname='mydiaryentries_testing' user='koin' host='localhost' " + "password='kiki'"
        self.db = Database()
        