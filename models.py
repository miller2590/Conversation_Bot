# import the datetime library
from datetime import datetime


class User:
    """The User class creates a user object after receiving
    name, age, and birth month from the user."""

    def __init__(self, name, age, birth_month):  # Self explanatory init function
        self.name = name
        self.age = age
        self.birth_month = birth_month
        self.created_date = datetime.now()

    # Repr function that will return user name, and age.
    def __repr__(self):
        return f'User: {self.name}, Age: {self.age}'
