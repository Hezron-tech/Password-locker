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

    def save_multiple_credential(self):
        self.new_credential.save_credential() 
        test_credential=Credential("FB","glovu","1234") 
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


        

    def delete_credentials(self):
        '''
        delete saved credentials in the credentials list
        '''
        Credential.credentials_list.remove(self)   



           


if __name__ == '__main__':
    unittest.main()
