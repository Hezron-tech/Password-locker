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

def display_user(user):
        return user.display_user()
                


def login_user(username,password):
    '''
    a fumction that checks if the users already exist 
    '''
    checked_user = Credential.verify_user(username,password)
    return checked_user


def delete_user(self):
        User.user_list.remove(self)   



def create_new_credential(account_name,Hezz,passcode):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Credential(account_name,Hezz,passcode)
    return new_credential

def save_credential(self):
        Credential.credential_list.append(self) 


def delete_credentials(self):
        '''
        delete saved credentials in the credentials list
        '''
        Credential.credential_list.remove(self)

def find_account(cls,account_name):
         for credential in cls.Credential.credential_list:
             if(credential.account_name==account_name):
                 return credential 


def verify_credential(account_name):
         """
           method used to verify credentials
         """
         for credential in Credential.Credential_list:
             if(credential.account_name==account_name):
                 return True
                 return False   


def generate_password(self):
    ''' 
    function tht generates password randomly
    '''
    auto_password = Credential.generate_password(self)
    return auto_password                                                 