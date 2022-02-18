import unittest
from users import User


class TestUsers(unittest,unittest.TestCase):

    def setUp(self):
        self.new_user=User("Hezzy","Kiprop")
        
    