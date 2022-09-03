#The User class is set up to hold the users name, email, password, and account type
class User:
    def __init__(self, name, email, password, account_type):
        self.name = name
        self.email = email
        self.password = password
        self.account_type = account_type

#This method will change the email of the specified user
    def change_email(self, new_email):
        self.email = new_email

#This method will change the password of the specified user       
    def change_password(self, new_password):
        self.password = new_password
