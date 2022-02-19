
from typing_extensions import Self


class Credentials:

    Credential_list=[]

    def __init__(self,user_password,credential_name):
        self.user_password=user_password
        self.credential_name=credential_name
