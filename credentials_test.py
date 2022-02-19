import unittest
from credentials import Credential

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_credential=Credential("Glovu","geek")
    def test_init(self):

        self.assertEqual(self.new_credential.account_name, "Glovu")
        self.assertEqual(self.new_credential.account_password, "geek")

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        Credential.credentials_list = []    
           


if __name__ == '__main__':
    unittest.main()
