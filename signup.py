from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox


# FUNCTIONS
def login_page():
    signup_window.destroy()
    import signin


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:  # For DB Connection Issues
        try:
            con = pymysql.connect(host='localhost', user='root', password='11010')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key, email varchar(20),username varchar(20), password varchar(20))'
            mycursor.execute(query)
        except:  # For no recreation of the same database
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query, usernameEntry.get())

        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already Exists')

        else:
            query = 'insert into data(email, username,password) values(%s,%s,%s)'
            value = (emailEntry.get(), usernameEntry.get(), passwordEntry.get())
            mycursor.execute(query, value)
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin


# GUI FOR SIGNUP PAGE
# Creating Window & Importing image
signup_window = Tk()
signup_window.title('SIGN-UP')
signup_window.resizable(0, 0)
background = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

# CREATING FRAME FOR CONTENTS OF SIGNUP PAGE
frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

# HEADING LABEL (inside FRAME CONTAINER)
heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold')
                , bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

# EMAIL LABEL
emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                   , fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
# EMAIL ENTRY
emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='black'
                   , bg='light grey')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

# USERNAME LABEL
usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                      , fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
# USERNAME ENTRY
usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='black'
                      , bg='light grey')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

# PASSWORD LABEL
passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                      , fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
# PASSWORD ENTRY
passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='black'
                      , bg='light grey')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

# CONFIRM LABEL
confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                     , fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
# CONFIRM ENTRY
confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='black'
                     , bg='light grey')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

# Terms & Conditions label and checkbox
check = IntVar()  # For checkbox condition
termsandconditions = Checkbutton(frame, text='I agree to The Terms & Conditions',
                                 font=('Microsoft Yahei UI Light', 8, 'bold'), fg='firebrick1',
                                 bg='white', activebackground='white', activeforeground='black', cursor='hand2',
                                 variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=15)

# SIGNUP BUTTON
signupButton = Button(frame, text='SIGNUP', font=('Open Sans', 16, 'bold'), bd=0, bg='dodgerblue2', fg='white',
                      activeforeground='firebrick1', activebackground='white', width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

# ALREADY HAVE ACCOUNT
alreadyaccount = Label(frame, text='already have Account?', font=('Open Sans', 9, 'bold'),
                       bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

# LOGIN BUTTON
loginButton = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), bg='white', fg='blue',
                     bd=0, activeforeground='blue', activebackground='white', cursor='hand2', command=login_page)
loginButton.place(x=170, y=402)

signup_window.mainloop()
