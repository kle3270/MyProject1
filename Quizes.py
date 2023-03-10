#Check If Login Already Exists
def LoginCheck(Username,Password,Userlist,Passlist):
    if Username in Userlist:
        if Password not in Passlist:
            print("Your password is incorrecet")
            Authentification = 0
        else:
            Authentification = 1
            print("Logging in...")
    else:
        print("Your account does not exist")
    return Authentification
