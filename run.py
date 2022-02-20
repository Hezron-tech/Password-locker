from users import User
from credentials import Credential


def save_user(username,password):
    '''

    function to add new user
    '''
    new_user=User(username,password)
    return new_user

def delete_user(username):
    User.delete_user(username)






def create_new_credential(account_name,email,passcode):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Credential(account_name,email,passcode)
    return new_credential