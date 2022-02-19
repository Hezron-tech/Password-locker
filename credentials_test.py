import pyperclip
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
        

    

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual( len(Credential.credential_list), 1) 



    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        Credential.credential_list=[]    
          



    def test_save_multiple_credentials(self):
        self.new_credential.save_credential() 
        test_credential=Credential("FB","glovu","1234") 
        test_credential.save_credential()
        self.assertEqual( len(Credential.credential_list), 2)


    def test_confirm_credentials_exists(self):
        '''
        confirm that credentials actually exists
        '''
        self.new_credential.save_credential()
        test_credential = Credential("FB", "glovu","1234")
        test_credential.save_credential()
        credentials_exists = Credential.credentials_exists("FB")
        self.assertTrue(credentials_exists)




##displaying the credentials
    def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)
        ##copy    





       

if __name__ == '__main__':
    unittest.main()
