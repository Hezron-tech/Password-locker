from users import User
from credentials import Credential


def create_user(username,password):
    '''

    function to add new user
    '''
    new_user=User(username,password)
    return new_user

def save_user(self):
        User.user_list.append(self)

def display_user(cls):
        return cls.user_list        







def login_user(username,password):
    '''
    a fumction that checks if the users already exist 
    '''
    checked_user = Credential.verify_user(username,password)
    return checked_user


def delete_user(self):
        User.user_list.remove(self)   
        
         

def create_new_credential(account_name,email,passcode):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Credential(account_name,email,passcode)
    return new_credential