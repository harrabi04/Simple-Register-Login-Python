from tkinter import *
from tkinter import messagebox
window= Tk()
DB="database.txt"
def Loginbut():
    loginv=login.get()
    print(loginv)
    password=pwd.get()
    print(password)
    info="usr_login="+loginv+"/usr_pwd="+password
    read=open(DB,'r')
    found=False
    for line in read:
        if info in line:
            found=True
        if found==True:
            messagebox.showinfo("login successful ")
        else:
            messagebox.showerror("login not found, Please try again")
    read.close()
def Regbutt():  
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
    return
login= StringVar()
pwd= StringVar()
window.iconbitmap()
window.geometry("400x400")
window.title("Password Checker")
#Login
label=Label(text='Login :', font=("Arial",20)).place(x=20,y=50, anchor=W )
loginiput=Entry(textvariable=login).place(x=20,y=80, anchor=W)
#Password
label=Label(text='Password :', font=("Arial",20)).place(x=210,y=50, anchor=W )
pwdiput=Entry(textvariable=pwd).place(x=210,y=80, anchor=W)
LoginButton= Button(text="Login" ,width=6, height=1, command=Loginbut).place(x=100,y=210, anchor=CENTER  )
'''label=Label(text='Password:', width=40, height=10).place(x=50,y=100, anchor=CENTER )
pwdiput=Entry(textvariable=pwd).place(x=25,y=120)
LoginButton= Button(text="Login" ,width=8, height=1, bd=5).place(x=250,y=280, anchor=CENTER  )'''


window.mainloop()

































'''confirmation='No'
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
'''

