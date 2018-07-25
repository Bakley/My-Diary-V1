import os
import jwt
import datetime

from passlib.apps import custom_app_context as pwd_context

from createdb_helper import Database



class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password
        self.user_id = 0
        self.conn = None
        self.cur = None
    
    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def create_user(self):
        database_connections = Database()
        columns = ("username",
                    "user_password",
                    "email"
        )
        values = (self.username,
                  self.password_hash,
                  self.email)

        data_returned = database_connections.insert("users", columns, values, "user_id")
        user_id = None
        for row in data_returned:
            user_id = row[0]

        return user_id

    @staticmethod
    def get_a_user(username):
        """Gets a user from the database, whose name matched the given username"""
        database_connections = Database()
        columns = "*"
        where = "username = \'" + username + "\'"
        data_returned = database_connections.select("users", columns, where=where)

        row = None
        if data_returned and len(data_returned) > 0:
            row = data_returned[0]
        
        user = None
        if row:
            user_id = row[0]
            username = row[1]
            password = row[2]
            email = row[3]
            user = User(username, password)
            user.email = email
            user.user_id = user_id
        return user

    
    def generate_auth_token(self):
        payload = {
            'user': self.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        }
        token = jwt.encode(payload, app.config['SECRET'], algorithm='HS256')

        return token

    @staticmethod
    def decode_token(token):
        """Used to decode a token obtained from the authorization header"""
        try:
            payload = jwt.decode(token,
                                 app.config['SECRET'],
                                 algorithms='HS256')
            return payload['user']
        except jwt.ExpiredSignature:
            return "Token is expired. Please login again"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"
