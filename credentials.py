
class Credential:

    credential_list=[]

    def __init__(self,account_name,username,account_password):
        self.account_name=account_name
        self.username=username
        self.account_password=account_password
        

    def save_credential(self):
        Credential.credential_list.append(self)



    def delete_credentials(self):
        '''
        delete saved credentials in the credentials list
        '''
        Credential.credentials_list.remove(self) 



    def create_credentials(account_name,email,passcode):
        new_credentials=Credential.credential_list(account_name,email,passcode) 
        return new_credentials  




    @classmethod
    def verify_credential(cls,account_name):
         """
           method used to verify credentials
         """
         for credential in Credential.Credential_list:
             if(credential.account_name==account_name):
                 return True
                 return False    

        
             


    @classmethod
    def find_account(cls,account_name):
         for credential in cls.Credential.Credential_list:
             if(credential.account_name==account_name):
                 return credential


    


    



       










