from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import ImageTk  # ImageTk class for loading bg image to the following window (login_window.mainliip())


# F-U-N-C-T-I-O-N Part ----------------------------------------------------------------------------------------------
def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Password & Confirm Password are not matching')
        else:
            con = pymysql.connect(host='localhost', user='root', password='11010', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()


    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel2 = Label(window, image=bgPic)
    bgLabel2.grid()

    # HEADING Label
    heading_label = Label(window, text='RESET PASSWORD', font=('arial', '18', 'bold'),
                          bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    # USERNAME Label
    userlabel = Label(window, text='Username', font=('arial', '12', 'bold'),
                          bg='white', fg='magenta2')
    userlabel.place(x=470, y=130)

    # USER ENTRY & FRAME
    user_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'),
                       bd=0)
    user_entry.place(x=470,y=160)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    # PASSWORD Label
    passwordlabel = Label(window, text='New Password', font=('arial', '12', 'bold'),
                          bg='white', fg='magenta2')
    passwordlabel.place(x=470, y=210)
    # Password ENTRY & FRAME
    newpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'),
                       bd=0)
    newpass_entry.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    # CONFIRM PASSWORD Label
    confirmpasslabel = Label(window, text='New Password', font=('arial', '12', 'bold'),
                          bg='white', fg='magenta2')
    confirmpasslabel.place(x=470, y=290)
    # Password ENTRY & FRAME
    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'),
                          bd=0)
    confirmpass_entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    # SUBMIT BUTTON
    submitButton = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('Open Sans', 16, 'bold'),
                          width=19, cursor='hand2', activebackground='magenta2', activeforeground='white', command=change_password)
    submitButton.place(x=470, y=390)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Fields are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1010')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'DB Connection Issue')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login is Successful')



def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


# G-R-A-P-H-I-C-S Part -----------------------------------------------------------------------------------------------

# CREATING MAIN WINDOW (LOGIN PAGE)
login_window = Tk()  # Tk() class to open background window
login_window.geometry(
    '990x660+50+50')  # placing the window from 50-50 positn from screen & fixing its size to image size(990x660)
login_window.resizable(0, 0)  # height and width not resizable
login_window.title('LOGIN PAGE')

# CREATING SIGNUP PAGE
bgImage = ImageTk.PhotoImage(file='bg.jpg')  # loading the image
bgLabel = Label(login_window, image=bgImage)  # creating label of the image & placing it in the login_window window
bgLabel.place(x=0, y=0)  # placing the label from 0,0 position of the login_window

# CREATING HEADING LABEL
heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold')
                , bg='white', fg='firebrick1')
heading.place(x=605, y=120)

# Entry Class for filling info
# USERNAME
usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                      , bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

# PASSWORD
passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                      , bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

# EYE Position
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white'
                   , cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

# FORGET BUTTON
forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white'
                   , cursor='hand2', command=forget_pass)
forgetButton.place(x=715, y=295)

# LOGIN BUTTON
loginButton=Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
                   fg='white', bg='firebrick1',activeforeground='white'
                   , cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

# -------OR-------
orLabel = Label(login_window, text=' --------------OR--------------', font=('Open Sans', 16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

# Google,FB,Twitter logos
facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='google.png')
ggLabel = Label(login_window, image=google_logo, bg='white')
ggLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='twitter.png')
twLabel = Label(login_window, image=twitter_logo, bg='white')
twLabel.place(x=740, y=440)

# SIGNUP LABEL & BUTTON
signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=590, y=500)

newaccountButton = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'),
                   fg='blue', bg='white',activeforeground='blue'
                   , activebackground='white', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727, y=500)

login_window.mainloop()

