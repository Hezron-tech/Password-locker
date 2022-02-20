#!/usr/bin/env python3.8

import pyperclip
 
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
    checked_user = Credential.login_user(username,password)
    return checked_user


def delete_user(self):
        User.user_list.remove(self) 


def display_credentials():
        '''
        method that returns all credentials
        '''
        return display_credentials          



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

def find_account(account_name):
    return Credential.find_account(account_name)
         


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
    function that generates password randomly
    '''
    auto_password = Credential.generate_password(self)
    return auto_password   

def main():
    print("Welcome to password locker!")
    print("Enter your name to start signing up")
    name = input ()
    print(f"{name}, Sign up to start")
    print('\n')
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("-" * 80)
    while True:
        
        short_code = input().lower()
        if short_code == 'cc':
            print("Account creating process begins...")
            print("Please enter the following information:")
            print("Username: ")
            username = input()
            print("Password: ")
            password = input()
            save_user(create_user(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)
            print("create new account, use:\n na--new account,\n  ex--existing account,\n")




            short_code = input("").lower().strip()

        if short_code=='na':
            print("Create new account i.e Facebook")
            print("Account name")
            account_name=input()
            print("username")
            username=input()
            print("password")
            password=""
            while True:
                print("Tp-type your password,\n Gp-generate password")
                pass_choice = input().lower().strip()
                if pass_choice=='tp':
                    print("\n")
                    
                    password=input("Enter password\n")
                    break
                
                elif pass_choice =='gp':
                    password = input(generate_password(password))
                    
                    break
                else:
                    print("Invalid password")

            save_user(create_user(username,password))
            print("-"*90)
            print(f"Hello {username}, Your {account_name} account  has been created succesfully created! Your password is: {password}")
            print("-"*90) 
        while True:
            print("To proceed select any:\n CC - Create a new credential  \n DS-Display your credentials \n FC - Find a credential \n D - Delete credential \n EX - Exit the application \n") 
            short_code = input().lower().strip()
            if short_code == "cc":
                print("Create new credentials")
                print("-"*80)
                print("Account name ....")
                account_name = input().lower()
                print("Your Account username")
                username = input()
                # while True:
                print(" TY - Type your own pasword if you already have an account:\n GR - Generate a random Password")
                password_Choice = input().lower().strip()
                if password_Choice=="ty":
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice=="GP":
                    password = generate_password(password)
                    break
                else:
                    print("invalid password")
                save_credential(create_new_credential(account_name,username,password))
                print('\n')
                print(f"Account Credential for:Account {account_name} :Username: {username} - Password:{password} created succesfully")
                print('\n')        
            if  short_code =="ds":
                print("ACCOUNT DETAILS ARE:")
                print(" "*30)

                for credential in display_credentials():
                    print(f"{credential.account_name}\n {credential.username}\n {credential.password}")
                else:

                    print("NO ACCOUNT!!!!")
            elif short_code=="fc":
                print("Which Account are you trying to find???")
                search_credentials= input()
                if find_account(search_credentials):
                    search_account=find_account(search_credentials)
                    print(f"{search_account.account_name}\n{search_account.username} \n {search_account.password}")
                else:
                    print("Account doesn't exist")
                    print('\n')
                    
                            
                      





# elif short_code=="da":
#             print(f"These are your credentials for {name}:")
#             print("*" * 30)
#             for Credentials in display_credentials():
#                     print(f"{Credentials.account}\n {Credentials.email}\n {Credentials.password}")
#             else:
#                     print("*" * 30)
#                     print("If empty, you do not have any accounts saved")
#                     ##find account
#         elif short_code == "fa":
#             print("Key in  the account you are searching for (ie.'instagram'): " )
#             search_credentials= input()
#             if find_account(search_credentials):
#                 search_acc = find_account(search_credentials)
#                 print(f"{search_acc.account} {search_acc.email} { search_acc.password}")
#             else: print("This account does not exist")



     


 

                                                         
if __name__ == '__main__':
     main()


