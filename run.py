from users import User
from credentials import Credential


def save_user(username,password):
    '''

    function to add new user
    '''
    new_user=User(username,password)
    return new_user
