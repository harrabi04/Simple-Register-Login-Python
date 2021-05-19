'''Python Login/Register BY MOATAZ HARRABI (https://github.com/harrabi04)'''
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
        messagebox.showinfo("Success","login successful")
    else:
        messagebox.showerror("login Error","login not found, Please try again")
    read.close()
def Regbutt():  
    newloginv = newlogin.get()
    newpasswordv = newpassword.get()
    password_checkv =password_check.get()
    if newpasswordv == password_checkv:
        newinfo = "usr_login=" + newloginv + "/usr_pwd=" + newpasswordv
        write = open(DB, 'a+')
        write.seek(0)
        data = write.read(10000)
        if len(data) > 0:
            write.write("\n"+newinfo)
        else:
            write.write(newinfo)
        write.close()
        messagebox.showinfo("Success", ("Account created succesfully"))
    else:
        messagebox.showwarning("Password conflit","password doesn't match")
    return
login= StringVar()
pwd= StringVar()
newpassword= StringVar()
newlogin= StringVar()
password_check= StringVar()
window.iconbitmap("login.ico")
window.geometry("400x400")
window.title("Login/Register")
#Register_Buttom_Label
label=Label(text='Login:', font=("Arial",20)).place(x=20,y=20, anchor=W )
LoginButton= Button(text="Login" ,width=6, height=1, command=Loginbut).place(x=20,y=135, anchor=W  )
#Email_Login
label=Label(text='Email:', font=("Arial",16)).place(x=20,y=65, anchor=W )
loginiput=Entry(textvariable=login).place(x=20,y=95, anchor=W)
#Password_Login
label=Label(text='Password :', font=("Arial",16)).place(x=210,y=65, anchor=W )
pwdiput=Entry(textvariable=pwd, show="*").place(x=210,y=95, anchor=W)
#Register_Buttom_Label
label=Label(text='Register:', font=("Arial",20)).place(x=20,y=190, anchor=W )
LoginButton= Button(text="Register" ,width=10, height=3, command=Regbutt).place(x=250,y=315, anchor=W  )
#Email_Register
label=Label(text='Email :', font=("Arial",16)).place(x=20,y=225, anchor=W )
loginiput=Entry(textvariable=newlogin).place(x=20,y=250, anchor=W)
#Password_Resgister
label=Label(text='Password :', font=("Arial",16)).place(x=20,y=285, anchor=W )
loginiput=Entry(textvariable=newpassword, show="*").place(x=20,y=310, anchor=W)
label=Label(text='Confirm Password :', font=("Arial",16)).place(x=20,y=345, anchor=W )
loginiput=Entry(textvariable=password_check, show="*").place(x=20,y=370, anchor=W)
window.mainloop()
