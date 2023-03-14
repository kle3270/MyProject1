import Quizes
import das
class User:
    def __init__(self,username,password,numberidentification):
        self.username = username
        self.password = password
        self.identifier = numberidentification
    def add_self(self):
        Users.append(self.username)
        return Users
    def password_add(self):
        Passwords.append(self.password)
    def store_age(self,age):
        self.age = age

numberidentification = 0
Users = []
Passwords = []
p1 = User("1","2",numberidentification)
p1.add_self()
p1.password_add()
Authentification = Quizes.LoginCheck("1","2",Users,Passwords)
if Authentification ==1:
    print("You have logged in")