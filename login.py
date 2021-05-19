'''Python Login/Register BY MOATAZ HARRABI (https://github.com/harrabi04)'''
from tkinter import *
from tkinter import messagebox
window= Tk()
DB="database.txt"
def Loginbut():
    loginv=login.get()
    password=pwd.get()
    logininput.delete(0,END)
    pwdinput.delete(0,END)
    info="usr_login="+loginv+"/usr_pwd="+password
    try:
        read=open(DB,'r')
    except:
        messagebox.showerror("login Error","login not found, Please try again")
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
    logininput2.delete(0,END)
    pwdinput2.delete(0,END)
    pwdinput3.delete(0,END)
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
logininput=Entry(textvariable=login)
logininput.place(x=20,y=95, anchor=W)
#Password_Login
label=Label(text='Password :', font=("Arial",16)).place(x=210,y=65, anchor=W )
pwdinput=Entry(textvariable=pwd, show="*")
pwdinput.place(x=210,y=95, anchor=W)
#Register_Buttom_Label
label=Label(text='Register:', font=("Arial",20)).place(x=20,y=190, anchor=W )
LoginButton= Button(text="Register" ,width=10, height=3, command=Regbutt).place(x=250,y=315, anchor=W  )
#Email_Register
label=Label(text='Email :', font=("Arial",16)).place(x=20,y=225, anchor=W )
logininput2=Entry(textvariable=newlogin)
logininput2.place(x=20,y=250, anchor=W)
#Password_Resgister
label=Label(text='Password :', font=("Arial",16)).place(x=20,y=285, anchor=W )
pwdinput2=Entry(textvariable=newpassword, show="*")
pwdinput2.place(x=20,y=310, anchor=W)
label=Label(text='Confirm Password :', font=("Arial",16)).place(x=20,y=345, anchor=W )
pwdinput3=Entry(textvariable=password_check, show="*")
pwdinput3.place(x=20,y=370, anchor=W)
window.mainloop()
