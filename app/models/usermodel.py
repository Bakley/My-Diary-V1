import os
import jwt
import datetime

from passlib.apps import custom_app_context as pwd_context
from .createdb_helper import Database
from app import app



class User():
    """Create the User model class"""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password

    
    def hash_password(self, password):
        """A method that will hash a password/secret,
        Uses the custom_app_context:LazyCryptContext"""
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        """A method that will verify a password/secret against the hashed a password/secret,
        Uses the custom_app_context:LazyCryptContext"""
        return pwd_context.verify(password, self.password_hash)

    def create_user(self):
        """A method that adds a new user to the database"""
        database_connections = Database()
        columns = ("username",
                    "password",
                    "email"
        )
        values = (self.username,
                  self.password_hash,
                  self.email)
        
        print("Values ==>", values)

        data_returned = database_connections.insert("users", columns, values)
        print("Data ===>", data_returned)

        return data_returned

    @staticmethod
    def get_a_user(username):
        """A staticmethod that gets a user from the database, whose name matched the given username"""
        database_connections = Database()
        columns = "*"
        where = "username = \'" + username + "\'"
        data_returned = database_connections.select("users", columns, where=where)
        print("User data", data_returned)
        # return data_returned

        row = None
        if data_returned and len(data_returned) > 0:
            row = data_returned[0]
        
        user = None
        if row:
            print("The user row", row)
            id = row[0]
            username = row[1]
            password = row[2]
            email = row[3]
            user = User(username, password, email)
            user.user_id = id
            
        return user

    
    def generate_auth_token(self):
        """A method used to generate access tokens"""
        payload = {
            'user': self.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        }
        token = jwt.encode(payload, app.config['SECRET'], algorithm='HS256')

        return token

    @staticmethod
    def decode_token(token):
        """A statis method used to decode a token obtained from the authorization header"""
        try:
            payload = jwt.decode(token,
                                 app.config['SECRET'],
                                 algorithms='HS256')
            return payload['user']
        except jwt.ExpiredSignature:
            return "Token is expired. Please login again"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"

# class Entries():
#     """Creates the Diary Entry Models"""

#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#         self.created_at = datetime.datetime.utcnow()
#         self.date_modified = datetime.datetime.utcnow()
        

#     def add_a_new_entry(self, user_id):
#         """A method which adds an entry associated to a specific user"""
#         database_connections = Database()
#         columns = ('user_id', 'title', 'description' 'created_at', 'date_modified')
#         values = (user_id, self.title, self.description, self.created_at, self.date_modified)

#         data_returned = database_connections.insert('entries', columns, values)

#         entry_id = None
#         for row in data_returned:
#             entry_id = row[0]

#         self.id = entry_id
#         return self.id

#     @staticmethod
#     def get_an_entry(entry_id):
#         """A static method that gets one entry"""
#         database_connections = Database()
#         columns = ('r.*', 'u.username')
#         tables = 'entry r'
#         left_join =  'users u on (u.user=r.user_id)'
#         where = 'r.entry_id = ' + str(entry_id)

#         data_returned = database_connections.select(tables, columns, left_join, where)

#         entry = None
#         if len(data_returned) == 0:
#             return entry

#         for row  in data_returned[0]:
#             row = tuple(row.replace("(", "").replace(")", "").split(","))
#             title = row[2]
#             description = row[3]
#             username = row[4].replace("\"", "")
#             entry = Entries(title, description)
#             entry_id = row[0]

#         return entry

