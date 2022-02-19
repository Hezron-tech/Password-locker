import unittest
from credentials import Credential

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_credential=Credential("Gmail","Hezzy","geek")
    def test_init(self):
        self.assertEqual(self.new_credential.account_name, "Gmail")
        self.assertEqual(self.new_credential.username,"Hezzy")
        self.assertEqual(self.new_credential.account_password, "geek")
        

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        Credential.credentials_list = []    
           


if __name__ == '__main__':
    unittest.main()
