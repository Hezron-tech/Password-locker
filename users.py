## create a class

class User:
    """generate an instance of a class
    """
    user_list=[]#list of users

    def __init__(self,username,password):
        self.username =username
        self.password =password
 

    ##save users
    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)


    @classmethod
    def verify_user(cls,username,password):
        a_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
                return a_user    

       

    @classmethod
    def find_by_user(cls,username):
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def display_user(cls):
        return cls.user_list            


 
      
   


       
    




