DB="database.txt"
print("---Welcome to Login Script---")
print("If you already have an account please type YES, if not type NO to register")
confirmation='No'
login=True
def answer():
    while True:
        global confirmation
        confirmation=input("Yes/No: ")
        if confirmation.upper() == "YES" or confirmation.upper() == "NO":
            break
        else:
            print("Please answer with yes or no")
def yes():
    while True:
        print("please enter your informations")
        login=input("Login: ")
        password=input("Password: ")
        info="usr_login="+login+"/usr_pwd="+password
        read=open(DB,'r')
        found=False
        for line in read:
            if info in line:
             found=True
        if found==True:
            print("login successful ")
            global T
            login=False
            break
        else:
             print("login not found, Please try again! ")
        read.close()
def no():
    print("Please enter your Informations")
    newlogin = input("Enter your Login: ")
    while True:
        newpassword = input("type a new password: ")
        password_check = input("Confirm your password: ")
        if newpassword == password_check:
            break
        else:
            print("password doesn't match")
    newinfo = "usr_login=" + newlogin + "/usr_pwd=" + newpassword
    write = open(DB, 'a+')
    write.seek(0)
    data = write.read(10000)
    if len(data) > 0:
        write.write("\n")
        write.write(newinfo)
    else:
        write.write(newinfo)
    write.close()
    print("account created successfully ")
    print("Do you want to login ?")
    answer()
answer()
while login==True:
    if confirmation.upper() == "YES":
        yes()
    if confirmation.upper() == "NO":
        no()
    if confirmation.upper() == "NO":
        break


