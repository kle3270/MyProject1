import sys
sys.path.append('../Read_write_etc')
import LoginFunction
import Password_Function
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
Username =input("Type in your username")
if Username in Users:
    existing_user = False
else:
    existing_user = True

"""numberidentification = 0
Users = []
Passwords = []
p1 = User("1","2",numberidentification)
add_1(numberidentification)
p1.add_self()
p1.password_add()
Authentification = LoginFunction.LoginCheck("1","2",Users,Passwords,getattr(p1,'identifier'))
if Authentification ==1:
    print("You have logged in")"""
#Login

#Sign Up
if not existing_user:
    print("Your username does not exist, lets create an account")
    Username = input("Type in a username: ")
    while Username in Users:
        print(f"{Username} is taken")
        Username = input("Type in a username:")
    password = input("Type in a password:")
    Password_Function.create_password(password)