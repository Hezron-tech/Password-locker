


class Credential:

    Credential_list=[]

    def __init__(self,account_name,username,account_password):
        self.account_name=account_name
        self.username=username
        self.account_password=account_password
        

    def save_credential(self):
        Credential.Credential_list.append(self)

    



    
            










