import re


class Validate:
    """This class contains code for validating user input"""

    @staticmethod
    def validate_username(username):
        """Just checks length of Username"""
        if len(username) < 5:
            return [False, "Username should be at least 5 characters"]
        return [True]

    @staticmethod
    def validate_password(password):
        """Just checks length of password"""
        if len(password) < 10:
            return [False,'Password should be at least 10 characters']
        return [True]

    @staticmethod
    def validate_email(email):
        """Checks if email is in correct format"""
        regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)"
        if re.match(regex, email, re.IGNORECASE):
            return [True]
        else:
            return [False, 'Email in wrong format']
