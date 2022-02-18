#!usr/bin/env python3.8
import unittest #import unittestmodule
from users import User #import the user class


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("Hezzy","#incorrect") #new User created


    


    def test_init(self):

        self.assertEqual(self.new_user.username, "Hezzy")
        self.assertEqual(self.new_user.password, "#incorrect")


        #function to test save users
    def test_save_user(self): 
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = [] 


          


    def test_save_multiple_users(self): 
        self.new_user.save_user()
        test_user =User("one","12334")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user =User("one","12334")
        test_user.save_user()
        test_user.delete_user()
        self.assertEqual(len(User.user_list),1)


    def test_find_user(self):
        self.new_user.save_user()
        test_user =User("one","12334")
        test_user.save_user()
        
        found_user=User.find_by_user("Hezzy")
        self.assertEqual(found_user.username,self.new_user.username)    



      

       


if __name__ == '__main__':
    unittest.main()



          

    