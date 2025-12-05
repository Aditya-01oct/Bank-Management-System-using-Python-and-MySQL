# importing important libraries

import tkinter as tk
import mysql.connector as mysql
from tkinter import *
from PIL import ImageTk, Image

# define global variables

uid = None
password = None

#establishing connection between python and mysql

connector = mysql.connect(host='localhost',
                          user = 'root',
                          passwd = 'Papaji',
                          database = 'Independent_Bank')

mycursor = connector.cursor()

# define main window

class main_window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        container = tk.Frame()
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.winfo_geometry()

        self.frames = {}

        for F in (HomePage,
                  EmpLoginPage,
                  EmpMenuPage,
                  EmpWithdrawPage,
                  EmpDepositPage,
                  EmpNewaccPage,
                  EmpBalancePage,
                  EmpDropPage,
                  EmpSignupPage,
                  CustLoginPage,
                  CustMenuPage,
                  CustWithdrawPage,
                  CustDepositPage,
                  CustBalancePage,
                  CustSignupPage,
                  NewaccPage,
                  AboutPage,
                  MorePage,
                  FeedbackPage):

            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=5,
                       column=5,
                       sticky='news')

        self.show_frame("HomePage")

    def show_frame(self,
                   page_name):
        
         #Show a frame for the given page name
        
         frame = self.frames[page_name]
         frame.tkraise()

# define Homepage window

class HomePage(tk.Frame):
    def __init__(self,parent,
                 controller):
        
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush',
                          height=1080,
                          width=1920)
        
        self.controller = controller
        
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times', 100, 'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        button1 = tk.Button(self, text="CUSTOMER LOGIN",
                            font = ("Times",30,"bold"),
                            foreground='black',
                            background='brown1',
                            command=lambda: controller.show_frame("CustLoginPage"))
        
        button1.place(x=100,y=200)

        button2 = tk.Button(self, text="EMPLOYEE LOGIN",
                            font = ("Times",30,"bold",),
                            foreground='black',
                            background='brown1',
                            command=lambda: controller.show_frame("EmpLoginPage"))
        
        button2.place(x=100, y=325)

        button4 = tk.Button(self, text="NEW ACCOUNT",
                            font = ("Times",30,"bold"),
                            foreground='black',
                            background='brown1',
                            command=lambda: controller.show_frame("NewaccPage"))
        
        button4.place(x=100, y=450)

        button5 = tk.Button(self, text="ABOUT",
                            font = ("Times",30,"bold"),
                            foreground='black',
                            background='brown1',
                            command=lambda: controller.show_frame("AboutPage"))
        
        button5.place(x=100, y=700)

        button6 = tk.Button(self, text="FEEDBACK",
                            font = ("Times",30,"bold"),
                            foreground='black',
                            background='brown1',
                            command=lambda: controller.show_frame("FeedbackPage"))
        
        button6.place(x=100, y=575)

        image1 = Image.open("C:\\Aditya\\Bank project\\logo.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test

        label1.place(x=100, y=30)

        image1 = Image.open("C:\\Aditya\\Bank project\\logo.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test

        label1.place(x=1350, y=30)

        image1 = Image.open("C:\\Aditya\\Bank project\\home.webp")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=550,width=900)
        label1.image = test

        label1.place(x=600, y=220)


# Define Employee LoginPage window

class EmpLoginPage(tk.Frame):

    def __init__(self,
                 parent,
                 controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250,y=0)

        Username_label = tk.Label(self,
                                  text="Enter Your Employee ID",
                                  font=('Times',30,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Username_label.place(x=50, y=200)

        Username_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',25,'bold'),
                                      foreground='black',
                                      background='white')
        Username_entry_box.place(x=100, y=270)

        Password_label = tk.Label(self,
                                  text="Enter Your PIN",
                                  font=('Times',30,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Password_label.place(x=50, y=340)

        Password_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',25,'bold'),
                                      background='white')
        Password_entry_box.place(x=100, y=410)
        
        Password_entry_box.configure(fg='black',
                                     show='*')
 
        Incorrect_label = tk.Label(self, text="",
                                   font=('Times',20,'bold'),
                                   foreground='red',
                                   background='lavender blush')
        Incorrect_label.place(x=50, y=480)

        image1 = Image.open("C:\\Aditya\\Bank project\\emplog.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=550,width=800)
        label1.image = test

        label1.place(x=600, y=200)

        def login(username,passwd):
               record = {}
               mycursor.execute('select uid,password from emplog')
               for row in mycursor:
                    record.update({row[0]:row[1]})

               all_users = list(record.keys())
               for user in all_users:
                   if user == username:
                        check_password = record[user]
                        if check_password == passwd:
                              return 'Correct ID'
                   else:
                        Incorrect_label['text'] = 'INCORRECT EMPLOYEE ID OR PASSWORD'

        def check_login():
            global uid
            uid = Username_entry_box.get()
            
            global password
            password = int(Password_entry_box.get())
            
            info = login(uid, password)

            if info == 'Correct ID':
                page = "EmpMenuPage"
                controller.show_frame(page)
                Incorrect_label['text'] = ''
                Username_entry_box.delete('0', 'end')
                Password_entry_box.delete('0', 'end')

        
        check_button = tk.Button(self,
                                 text='LOGIN',
                                 relief='raised',
                                 height=1,
                                 width=6,
                                 font=('Times',20,'bold'),
                                 foreground='black',
                                 background='brown1',
                                 command=check_login)
        check_button.place(x=50, y=600)

        def login_exit():
            Incorrect_label['text'] = ''
            Username_entry_box.delete('0', 'end')
            Password_entry_box.delete('0', 'end')
            controller.show_frame("HomePage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=600)

# Define Employee menu page

class EmpMenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self, text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                            bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        def withdraw():
            controller.show_frame('EmpWithdrawPage')

        withdraw_button = tk.Button(bottom_frame,
                                    text='AMOUNT WITHDRAW',
                                    command=withdraw,
                                    relief='raised',
                                    font=('Times',20,'bold'),
                                    bg='BROWN1')
        withdraw_button.place(x=250, y=100)

        def Deposit():
            controller.show_frame('EmpDepositPage')

        deposit_button = tk.Button(bottom_frame,
                                   text='AMOUNT DEPOSITE',
                                   command=Deposit,
                                    relief='raised',
                                   font=('Times',20,'bold'),
                                   bg='brown1')
        deposit_button.place(x=800, y=100)

        def statement():
            controller.show_frame('EmpBalancePage')

        statement_button = tk.Button(bottom_frame,
                                   text='CURRENT BALANCE',
                                   command=statement,
                                    relief='raised',
                                    font=('Times',20,'bold'),
                                    bg='brown1')
        statement_button.place(x=250, y=300)

        def addacc():
            controller.show_frame('EmpNewaccPage')

        addacc_button = tk.Button(bottom_frame,
                                   text='NEW ACCOUNT',
                                   command=addacc,
                                    relief='raised',
                                  font=('Times',20,'bold'),
                                    bg='brown1')
        addacc_button.place(x=250, y=200)

        def delacc():
            controller.show_frame('EmpDropPage')

        delacc_button = tk.Button(bottom_frame,
                                   text='DELETE ACCOUNT',
                                   command=delacc,
                                    relief='raised',
                                  font=('Times',20,'bold'),
                                    bg='brown1')
        delacc_button.place(x=800, y=200)

        def Exit():
            controller.show_frame('HomePage')

        exit_button = tk.Button(bottom_frame,
                                text='LOG OUT',
                                command=Exit,
                                relief='raised',
                                font=('Times',20,'bold'),
                                bg='brown1')
        exit_button.place(x=800, y=300)


# Define EmpWithdrawPage
class EmpWithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller

        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        uid_label = tk.Label(bottom_frame,
                                   text='Please Enter Customer ID',
                                   font=('Times',30,'bold',),
                                   foreground='black',
                                   bg='lavender blush')
        uid_label.place(x=50, y=50)

        uid_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        uid_entry_box.place(x=70, y=125)

        Money_label = tk.Label(bottom_frame,
                               text="Enter Amount To Withdraw",
                               font=('Times',30,'bold'),
                               foreground='black',
                               background='lavender blush')
        Money_label.place(x=50, y=180)

        Money_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        Money_entry_box.place(x=70, y=250)

        image1 = Image.open("C:\\Aditya\\Bank project\\empwith.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=600)
        label1.image = test

        label1.place(x=700, y=320)

        def subtract_money():
            uid = uid_entry_box.get()
            Withdrawn_money = Money_entry_box.get()
            mycursor.execute('UPDATE cust SET money=money-{0} WHERE \
                              uid="{1}"'.format(Withdrawn_money, uid))
            connector.commit()

            uid_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')
            
            controller.show_frame("EmpMenuPage")

        enter_button = tk.Button(bottom_frame,
                                 text='ENTER',
                                 relief='raised',
                                 font = ("Times",20,"bold"),
                            foreground='black',
                            background='brown1',
                                 command=subtract_money)
        enter_button.place(x=100, y=350)


        def login_exit():
            uid_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')
            controller.show_frame("EmpMenuPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=650)

class EmpDepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        uid_label = tk.Label(bottom_frame,
                                   text='Please Enter Customer ID',
                                   font=('Times',30,'bold',),
                                   foreground='black',
                                   bg='lavender blush')
        uid_label.place(x=50, y=50)

        uid_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        uid_entry_box.place(x=70, y=125)

        Money_label = tk.Label(bottom_frame,
                               text="Enter Amount To Deposit",
                               font=('Times',30,'bold'),
                               foreground='black',
                               background='lavender blush')
        Money_label.place(x=50, y=180)

        Money_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        Money_entry_box.place(x=70, y=250)

        image1 = Image.open("C:\\Aditya\\Bank project\\empdepo.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=750)
        label1.image = test

        label1.place(x=600, y=320)

        def add_money():
            uid = uid_entry_box.get()
            Withdrawn_money = Money_entry_box.get()
            mycursor.execute('UPDATE cust SET money=money+{0} WHERE \
                              uid="{1}"'.format(Withdrawn_money, uid))
            connector.commit()

            uid_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')
            
            controller.show_frame("EmpMenuPage")

        enter_button = tk.Button(bottom_frame,
                                 text='ENTER',
                                 relief='raised',
                                 font = ("Times",20,"bold"),
                            foreground='black',
                            background='brown1',
                                 command=add_money)
        enter_button.place(x=50, y=350)

        def login_exit():

            uid_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')
            
            controller.show_frame("EmpMenuPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=650)

class EmpBalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller

        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        uid_label = tk.Label(bottom_frame,
                                   text='Please Enter Customer ID',
                                   font=('Times',30,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        uid_label.place(x=50, y=50)

        uid_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        uid_entry_box.place(x=50, y=125)

        image1 = Image.open("C:\\Aditya\\Bank project\\custbal.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=750)
        label1.image = test

        label1.place(x=600, y=320)

        current_balance = 0
        
        def current():
                uid = uid_entry_box.get()
                record = {}
                mycursor.execute('select uid,money from cust')
                for row in mycursor:
                   record.update({row[0]:row[1]})

                all_users = record.keys()
                for user in all_users:
                     if user == uid:
                         current_balance = record[user]
                         Show_Balance['text'] = current_balance

        Balance_label = tk.Button(bottom_frame,
                                  text="Current Balance",
                                  font=('Times',25,'bold'),
                                  foreground='black',
                                  background='brown1',
                                  command=current)
        Balance_label.place(x=80, y=200)

        Show_Balance = tk.Label(bottom_frame,
                                text='',
                                font=('Times',20,'bold'),
                                foreground='black',
                                background='white',
                                bd=2,
                                height=2,
                                width=15)
        Show_Balance.place(x=100, y=300)

        def balance_exit():
            Show_Balance['text'] = ''
            uid_entry_box.delete('0','end')
            controller.show_frame("EmpMenuPage")

        def login_exit():
            
            Show_Balance['text'] = ''
            uid_entry_box.delete('0','end')
            controller.show_frame("EmpMenuPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=200,y=700)

class EmpDropPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        uid_label = tk.Label(bottom_frame,
                                   text='Please Enter Customer ID',
                                   font=('Times',30,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        uid_label.place(x=50, y=50)

        uid_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        uid_entry_box.place(x=50, y=125)
        
        image1 = Image.open("C:\\Aditya\\Bank project\\OIP2.jpeg.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=750)
        label1.image = test

        label1.place(x=600, y=320)

        def Drop():
            uid = uid_entry_box.get()
            mycursor.execute('Delete from cust WHERE \
                              uid="{0}"'.format(uid))
            connector.commit()

            uid_entry_box.delete('0','end')
            
            controller.show_frame("EmpMenuPage")

        enter_button = tk.Button(self,
                                 text='Delete',
                                 relief='raised',
                                 font = ("Times",20,"bold"),
                            foreground='black',
                            background='brown1',
                                 command=Drop)
        enter_button.place(x=50, y=600)

        def login_exit():
            uid_entry_box.delete('0','end')
            controller.show_frame("EmpMenuPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=250,y=600)

class EmpNewaccPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        headinglabel = tk.Label(self,
                                text="NEW ACCOUNT",
                                anchor='center',
                                font=('Times',50,'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=500, y=200)
        
        Username_label = tk.Label(self,
                                  text="Please Enter Customer's Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Username_label.place(x=20, y=300)

        Username_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        Username_entry_box.place(x=450, y=300)

        fUsername_label = tk.Label(self,
                                  text="Enter Customer's Father's Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        fUsername_label.place(x=20, y=350)

        fUsername_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        fUsername_entry_box.place(x=450, y=350)

        mUsername_label = tk.Label(self,
                                  text="Enter Customer's Mother's Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        mUsername_label.place(x=20, y=400)

        mUsername_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        mUsername_entry_box.place(x=450, y=400)

        mobile_label = tk.Label(self,
                                  text="Enter Customer's Mobile Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        mobile_label.place(x=20, y=450)

        mobile_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        mobile_entry_box.place(x=450, y=450)

        mail_label = tk.Label(self,
                                  text="Enter Customer's E-mail ID",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        mail_label.place(x=20, y=500)

        mail_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        mail_entry_box.place(x=450, y=500)

        gender_label = tk.Label(self,
                                  text="Enter Customer's Gender",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        gender_label.place(x=20, y=550)

        gender_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        gender_entry_box.place(x=450, y=550)

        dob_label = tk.Label(self,
                                  text="Enter Customer's Date Of Birth",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        dob_label.place(x=20, y=600)

        dob_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        dob_entry_box.place(x=450, y=600)

        addres_label = tk.Label(self,
                                  text="Enter Customer's Address",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        addres_label.place(x=800, y=300)

        addres_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        addres_entry_box.place(x=1200, y=300)

        aadhar_label = tk.Label(self,
                                  text="Enter Aadhar Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        aadhar_label.place(x=800, y=350)

        aadhar_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        aadhar_entry_box.place(x=1200, y=350)

        nominame_label = tk.Label(self,
                                  text="Enter Nominee Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nominame_label.place(x=800, y=400)

        nominame_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        nominame_entry_box.place(x=1200, y=400)

        nomiaadhar_label = tk.Label(self,
                                  text="Enter Nominee Aadhar Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nomiaadhar_label.place(x=800, y=450)

        nomiaadhar_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        nomiaadhar_entry_box.place(x=1200, y=450)

        nomimobile_label = tk.Label(self,
                                  text="Enter Nominee Mobile Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nomimobile_label.place(x=800, y=500)

        nomimobile_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        nomimobile_entry_box.place(x=1200, y=500)

        nomimail_label = tk.Label(self,
                                  text="Enter Nominee E-mail ID",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nomimail_label.place(x=800, y=550)

        nomimail_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        nomimail_entry_box.place(x=1200, y=550)

        branch_label = tk.Label(self,
                                  text="Enter Your Branch Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        branch_label.place(x=800, y=600)

        branch_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        branch_entry_box.place(x=1200, y=600)

        def login_exit():
            mUsername_entry_box.delete('0','end')
            fUsername_entry_box.delete('0','end')
            Username_entry_box.delete('0','end')
            mobile_entry_box.delete('0','end')
            gender_entry_box.delete('0','end')
            mail_entry_box.delete('0','end')
            dob_entry_box.delete('0','end')
            addres_entry_box.delete('0','end')
            aadhar_entry_box.delete('0','end')
            nominame_entry_box.delete('0','end')
            nomiaadhar_entry_box.delete('0','end')
            nomimobile_entry_box.delete('0','end')
            nomimail_entry_box.delete('0','end')
            branch_entry_box.delete('0','end')
            controller.show_frame("EmpMenuPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=800,y=700)

        
        def signup(name,fname,mname,mobile,mail,
                   gender,dob,addres,aadhar,nominame,nomiaadhar,nomimobile,nomimail,branch):
            mycursor.execute('insert into custlog values\
("{0}","{1}","{2}","{3}","{4}","{5}",\
"{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}")'\
                             .format(name,fname,mname,mobile,mail,gender,
                        dob,addres,aadhar,nominame,nomiaadhar,nomimobile,nomimail,branch))
            connector.commit()
        def signup_command():
            name = Username_entry_box.get()
            fname = fUsername_entry_box.get()
            mname = mUsername_entry_box.get()
            mobile = mobile_entry_box.get()
            mail = mail_entry_box.get()
            gender = gender_entry_box.get()
            dob = dob_entry_box.get()
            addres = addres_entry_box.get()
            aadhar = aadhar_entry_box.get()
            nominame = nominame_entry_box.get()
            nomiaadhar = nomiaadhar_entry_box.get()
            nomimobile = nomimobile_entry_box.get()
            nomimail = nomimail_entry_box.get()
            branch = branch_entry_box.get()
            

            signup(name,fname,mname,mobile,mail,
                   gender,dob,addres,aadhar,nominame,nomiaadhar,nomimobile,nomimail,branch)

            mUsername_entry_box.delete('0','end')
            fUsername_entry_box.delete('0','end')
            Username_entry_box.delete('0','end')
            mobile_entry_box.delete('0','end')
            gender_entry_box.delete('0','end')
            mail_entry_box.delete('0','end')
            dob_entry_box.delete('0','end')
            addres_entry_box.delete('0','end')
            aadhar_entry_box.delete('0','end')
            nominame_entry_box.delete('0','end')
            nomiaadhar_entry_box.delete('0','end')
            nomimobile_entry_box.delete('0','end')
            nomimail_entry_box.delete('0','end')
            branch_entry_box.delete('0','end')

            controller.show_frame("EmpSignupPage")


        signup_button = tk.Button(self, text='NEXT',
                                  font=('Times', 30, 'bold'),
                                  foreground='black',
                                  background='brown1',
                                  relief='raised',
                                  command=signup_command)
        signup_button.place(x=300,y=700)


class EmpSignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        Username_label = tk.Label(self,
                                  text="Enter your customer id\n\
(Tell Your Customer to Remember it)"
                                  , font=('Times',25,'bold')
                                  , foreground='crimson',
                                  background='lavender blush')
        Username_label.place(x=0, y=200)

        Username_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',25,'bold'))
        Username_entry_box.place(x=100, y=300)

        Password_label = tk.Label(self,
                                  text="Enter New PIN\n\
(Tell Your Customer to Remember it)",
                                  font=('Times',25,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Password_label.place(x=0, y=350)

        Password_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',25,'bold'))
        Password_entry_box.place(x=100, y=450)

        Money_label = tk.Label(self,
                               text="Enter Minimum Amount to deposit\n\
(Ask Minimum Amount From Your Customer)",
                               font=('Times',25,'bold'),
                               foreground='crimson',
                               background='lavender blush')
        Money_label.place(x=0, y=500)

        Money_entry_box = tk.Entry(self,
                                   textvariable=tk.IntVar,
                                   font=('Times',25,'bold'))
        Money_entry_box.place(x=100, y=600)

        image1 = Image.open("C:\\Aditya\\Bank project\\SECURITY.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=500,width=800)
        label1.image = test

        label1.place(x=700, y=200)

        def signup(uid, password, money):
            mycursor.execute('insert into cust values("{0}",{1}\
,{2})'.format(uid, password, money ))
            connector.commit()
        def signup_command():
            user_id = Username_entry_box.get()
            password = Password_entry_box.get()
            money = Money_entry_box.get()

            signup(user_id, password, money)

            Username_entry_box.delete('0','end')
            Password_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')

            controller.show_frame("HomePage")

        signup_button = tk.Button(self,
                                  text='CREATE',
                                  relief='raised',
                                  font=('Times',30,'bold'),
                                  bg='brown1',
                                  command=signup_command)
        signup_button.place(x=25,y=700)

        def Exit():

            Username_entry_box.delete('0','end')
            Password_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')
            
            controller.show_frame('EmpMenuPage')

        exit_button = tk.Button(self,
                                text='EXIT',
                                command=Exit,
                                relief='raised',
                                font=('Times',30,'bold'),
                                bg='brown1')
        exit_button.place(x=400, y=700)

# Define Customer Login Page Window

class CustLoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250,y=0)

        Username_label = tk.Label(self,
                                  text="Enter Your Customer ID",
                                  font=('Times',30,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Username_label.place(x=50, y=200)

        Username_entry_box = tk.Entry(self,textvariable=tk.StringVar,
                                      font=('Times',25,'bold'),
                                      foreground='black',
                                      background='white')
        Username_entry_box.place(x=100, y=270)

        Password_label = tk.Label(self,
                                  text="Enter Your PIN",
                                  font=('Times',30,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Password_label.place(x=50, y=340)

        Password_entry_box = tk.Entry(self, textvariable=tk.IntVar,
                                      font=('Times',25,'bold'),
                                      background='white')
        Password_entry_box.place(x=100, y=410)
        
        Password_entry_box.configure(fg='black', show='*')
 
        Incorrect_label = tk.Label(self, text="", font=('Times',20,'bold'),
                                   foreground='red', background='lavender blush')
        Incorrect_label.place(x=50, y=480)


        image1 = Image.open("C:\\Aditya\\Bank project\\custlog.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=550,width=800)
        label1.image = test

        label1.place(x=600, y=200)

        def login(username,passwd):
               record = {}
               mycursor.execute('select uid,password from cust')
               for row in mycursor:
                    record.update({row[0]:row[1]})

               all_users = list(record.keys())
               for user in all_users:
                   if user == username:
                        check_password = record[user]
                        if check_password == passwd:
                              return 'Correct ID'
                   else:
                        Incorrect_label['text'] = 'INCORRECT PASSWORD OR USERNAME'

        def check_login():
            global uid
            uid = Username_entry_box.get()
            
            global password
            password = int(Password_entry_box.get())
            
            info = login(uid, password)

            if info == 'Correct ID':
                page = "CustMenuPage"
                controller.show_frame(page)
                Incorrect_label['text'] = ''
                Username_entry_box.delete('0', 'end')
                Password_entry_box.delete('0', 'end')

        
        check_button = tk.Button(self,
                                 text='LOGIN',
                                 relief='raised',
                                 height=1,
                                 width=6,
                                 font=('Times',20,'bold'),
                                 foreground='black',
                                 background='brown1',
                                 command=check_login)
        check_button.place(x=50, y=600)

        def login_exit():
            Incorrect_label['text'] = ''
            Username_entry_box.delete('0', 'end')
            Password_entry_box.delete('0', 'end')
            controller.show_frame("HomePage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=600)

# Define Customer menu page window

class CustMenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self, text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                            bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        def withdraw():
            controller.show_frame('CustWithdrawPage')

        withdraw_button = tk.Button(bottom_frame,
                                    text='AMOUNT WITHDRAW',
                                    command=withdraw,
                                    relief='raised',
                                    font=('Times',20,'bold'),
                                    bg='BROWN1')
        withdraw_button.place(x=250, y=100)

        def Deposit():
            controller.show_frame('CustDepositPage')

        deposit_button = tk.Button(bottom_frame,
                                   text='AMOUNT DEPOSITE',
                                   command=Deposit,
                                    relief='raised',
                                   font=('Times',20,'bold'),
                                   bg='brown1')
        deposit_button.place(x=700, y=100)

        def balance():
            controller.show_frame('CustBalancePage')

        balance_button = tk.Button(bottom_frame,
                                   text='CURRENT BALANCE',
                                   command=balance,
                                    relief='raised',
                                    font=('Times',20,'bold'),
                                    bg='brown1')
        balance_button.place(x=250, y=300)

        def Exit():
            controller.show_frame('HomePage')

        exit_button = tk.Button(bottom_frame,
                                text='LOG OUT',
                                command=Exit,
                                relief='raised',
                                font=('Times',20,'bold'),
                                bg='brown1')
        exit_button.place(x=700, y=300)

    

# Define customer withdraw page

class CustWithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller

        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        Money_label = tk.Label(bottom_frame,
                               text="Enter Amount To Withdraw",
                               font=('Times',30,'bold'),
                               foreground='black',
                               background='lavender blush')
        Money_label.place(x=50, y=50)

        Money_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        Money_entry_box.place(x=50, y=150)

        image1 = Image.open("C:\\Aditya\\Bank project\\custwith.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=750)
        label1.image = test

        label1.place(x=600, y=320)

        def subtract_money():
            global uid
            Withdrawn_money = Money_entry_box.get()
            mycursor.execute('UPDATE cust SET money=money-{0} WHERE \
                              uid="{1}"'.format(Withdrawn_money, uid))
            connector.commit()

            Money_entry_box.delete('0','end')
            
            controller.show_frame("CustMenuPage")

        enter_button = tk.Button(bottom_frame,
                                 text='ENTER',
                                 relief='raised',
                                 font = ("Times",20,"bold"),
                            foreground='black',
                            background='brown1',
                                 command=subtract_money)
        enter_button.place(x=50, y=300)


        def login_exit():
            Money_entry_box.delete('0','end')
            controller.show_frame("CustMenuPage")

        Start_page_button = tk.Button(bottom_frame,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=300)

class CustDepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        Money_label = tk.Label(bottom_frame,
                               text="Enter Amount To Deposit",
                               font=('Times',30,'bold'),
                               foreground='black',
                               background='lavender blush')
        Money_label.place(x=50, y=50)

        Money_entry_box = tk.Entry(bottom_frame,
                                   textvariable=tk.IntVar,
                                   font=('Times',30,'bold'))
        Money_entry_box.place(x=50, y=150)

        image1 = Image.open("C:\\Aditya\\Bank project\\custdepo.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=750)
        label1.image = test

        label1.place(x=600, y=320)

        def add_money():
            global uid
            Withdrawn_money = Money_entry_box.get()
            mycursor.execute('UPDATE cust SET money=money+{0} WHERE \
                              uid="{1}"'.format(Withdrawn_money, uid))
            connector.commit()

            Money_entry_box.delete('0','end')
            
            controller.show_frame("CustMenuPage")

        enter_button = tk.Button(bottom_frame,
                                 text='ENTER',
                                 relief='raised',
                                 font = ("Times",20,"bold"),
                            foreground='black',
                            background='brown1',
                                 command=add_money)
        enter_button.place(x=50, y=300)

        def login_exit():

            Money_entry_box.delete('0','end')
            
            controller.show_frame("CustMenuPage")

        Start_page_button = tk.Button(bottom_frame,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=300)

class CustBalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller

        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')
        headinglabel.place(x=250, y=0)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('Times',70,'bold'),
                                   foreground='black',
                                   bg='lavender blush')
        main_menu_label.place(x=500, y=170)

        bottom_frame = tk.Frame(self,
                                bg='lavender blush',
                                height=800,
                                width=1920)
        bottom_frame.place(y=300)

        image1 = Image.open("C:\\Aditya\\Bank project\\custbal.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=400,width=750)
        label1.image = test

        label1.place(x=600, y=320)

        current_balance = 0
        
        def current():
                global uid
                record = {}
                mycursor.execute('select uid,money from cust')
                for row in mycursor:
                   record.update({row[0]:row[1]})

                all_users = record.keys()
                for user in all_users:
                     if user == uid:
                         current_balance = record[user]
                         Show_Balance['text'] = current_balance

        Balance_label = tk.Button(bottom_frame,
                                  text="Current Balance",
                                  font=('Times',30,'bold'),
                                  foreground='black',
                                  background='brown1',
                                  command=current)
        Balance_label.place(x=100, y=100)

        Show_Balance = tk.Label(bottom_frame,
                                text='',
                                font=('Times',20,'bold'),
                                foreground='black',
                                background='white',
                                bd=2,
                                height=2,
                                width=15)
        Show_Balance.place(x=100, y=200)

        def balance_exit():
            Show_Balance['text'] = ''
            controller.show_frame("CustMenuPage")

        def login_exit():
            Show_Balance['text'] = ''
            controller.show_frame("CustMenuPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',20,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=150,y=650)


# Define Customer Sign up Page window

class CustSignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        Username_label = tk.Label(self,
                                  text="Enter your customer id\n\
(remember as everytime you login you need it)"
                                  , font=('Times',25,'bold')
                                  , foreground='crimson',
                                  background='lavender blush')
        Username_label.place(x=0, y=200)

        Username_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',25,'bold'))
        Username_entry_box.place(x=100, y=300)

        Password_label = tk.Label(self,
                                  text="Enter New PIN\n\
(remember as everytime you login you need it)",
                                  font=('Times',25,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Password_label.place(x=0, y=350)

        Password_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',25,'bold'))
        Password_entry_box.place(x=100, y=450)

        Money_label = tk.Label(self,
                               text="Enter Minimum Amount to deposit\n\
(To Start Your Banking Services Now)",
                               font=('Times',25,'bold'),
                               foreground='crimson',
                               background='lavender blush')
        Money_label.place(x=0, y=500)

        Money_entry_box = tk.Entry(self,
                                   textvariable=tk.IntVar,
                                   font=('Times',25,'bold'))
        Money_entry_box.place(x=100, y=600)

        image1 = Image.open("C:\\Aditya\\Bank project\\SECURITY.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self,image=test,height=500,width=800)
        label1.image = test

        label1.place(x=700, y=200)

        def signup(uid, password, money):
            mycursor.execute('insert into cust values("{0}",{1}\
,{2})'.format(uid, password, money ))
            connector.commit()
        def signup_command():
            user_id = Username_entry_box.get()
            password = Password_entry_box.get()
            money = Money_entry_box.get()

            signup(user_id, password, money)

            Username_entry_box.delete('0','end')
            Password_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')

            controller.show_frame("HomePage")

        signup_button = tk.Button(self,
                                  text='CREATE',
                                  relief='raised',
                                  font=('Times',30,'bold'),
                                  bg='brown1',
                                  command=signup_command)
        signup_button.place(x=25,y=700)

        def Exit():

            Username_entry_box.delete('0','end')
            Password_entry_box.delete('0','end')
            Money_entry_box.delete('0','end')
            
            controller.show_frame('HomePage')

        exit_button = tk.Button(self,
                                text='EXIT',
                                command=Exit,
                                relief='raised',
                                font=('Times',30,'bold'),
                                bg='brown1')
        exit_button.place(x=400, y=700)

# Define New Account Page window

class NewaccPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,
                          parent,
                          bg='lavender blush')
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times',100,'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        headinglabel = tk.Label(self,
                                text="NEW ACCOUNT",
                                anchor='center',
                                font=('Times',50,'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=500, y=200)
        
        Username_label = tk.Label(self,
                                  text="Enter Your Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        Username_label.place(x=50, y=300)

        Username_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        Username_entry_box.place(x=400, y=300)

        fUsername_label = tk.Label(self,
                                  text="Enter Your Father's Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        fUsername_label.place(x=50, y=350)

        fUsername_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        fUsername_entry_box.place(x=400, y=350)

        mUsername_label = tk.Label(self,
                                  text="Enter Your Mother's Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        mUsername_label.place(x=50, y=400)

        mUsername_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        mUsername_entry_box.place(x=400, y=400)

        mobile_label = tk.Label(self,
                                  text="Enter Your Mobile Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        mobile_label.place(x=50, y=450)

        mobile_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        mobile_entry_box.place(x=400, y=450)

        mail_label = tk.Label(self,
                                  text="Enter Your E-mail ID",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        mail_label.place(x=50, y=500)

        mail_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        mail_entry_box.place(x=400, y=500)

        gender_label = tk.Label(self,
                                  text="Enter Your Gender",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        gender_label.place(x=50, y=550)

        gender_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        gender_entry_box.place(x=400, y=550)

        dob_label = tk.Label(self,
                                  text="Enter Your Date Of Birth",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        dob_label.place(x=50, y=600)

        dob_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        dob_entry_box.place(x=400, y=600)

        addres_label = tk.Label(self,
                                  text="Enter Your Address",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        addres_label.place(x=700, y=300)

        addres_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        addres_entry_box.place(x=1100, y=300)

        aadhar_label = tk.Label(self,
                                  text="Enter Your Aadhar Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        aadhar_label.place(x=700, y=350)

        aadhar_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        aadhar_entry_box.place(x=1100, y=350)

        nominame_label = tk.Label(self,
                                  text="Enter Nominee Name",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nominame_label.place(x=700, y=400)

        nominame_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        nominame_entry_box.place(x=1100, y=400)

        nomiaadhar_label = tk.Label(self,
                                  text="Enter Nominee Aadhar Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nomiaadhar_label.place(x=700, y=450)

        nomiaadhar_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        nomiaadhar_entry_box.place(x=1100, y=450)

        nomimobile_label = tk.Label(self,
                                  text="Enter Nominee Mobile Number",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nomimobile_label.place(x=700, y=500)

        nomimobile_entry_box = tk.Entry(self,
                                      textvariable=tk.IntVar,
                                      font=('Times',20,'bold'))
        nomimobile_entry_box.place(x=1100, y=500)

        nomimail_label = tk.Label(self,
                                  text="Enter Nominee E-mail ID",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        nomimail_label.place(x=700, y=550)

        nomimail_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        nomimail_entry_box.place(x=1100, y=550)

        branch_label = tk.Label(self,
                                  text="Enter Your Nearest Branch",
                                  font=('Times',20,'bold'),
                                  foreground='crimson',
                                  background='lavender blush')
        branch_label.place(x=700, y=600)

        branch_entry_box = tk.Entry(self,
                                      textvariable=tk.StringVar,
                                      font=('Times',20,'bold'))
        branch_entry_box.place(x=1100, y=600)

        def login_exit():
            mUsername_entry_box.delete('0','end')
            fUsername_entry_box.delete('0','end')
            Username_entry_box.delete('0','end')
            mobile_entry_box.delete('0','end')
            gender_entry_box.delete('0','end')
            mail_entry_box.delete('0','end')
            dob_entry_box.delete('0','end')
            addres_entry_box.delete('0','end')
            aadhar_entry_box.delete('0','end')
            nominame_entry_box.delete('0','end')
            nomiaadhar_entry_box.delete('0','end')
            nomimobile_entry_box.delete('0','end')
            nomimail_entry_box.delete('0','end')
            branch_entry_box.delete('0','end')
            controller.show_frame("HomePage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=800,y=700)

        
        def signup(name,fname,mname,mobile,mail,
                   gender,dob,addres,aadhar,nominame,nomiaadhar,nomimobile,nomimail,branch):
            mycursor.execute('insert into custlog values\
("{0}","{1}","{2}","{3}","{4}","{5}",\
"{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}")'\
                             .format(name,fname,mname,mobile,mail,gender,
                        dob,addres,aadhar,nominame,nomiaadhar,nomimobile,nomimail,branch))
            connector.commit()
        def signup_command():
            name = Username_entry_box.get()
            fname = fUsername_entry_box.get()
            mname = mUsername_entry_box.get()
            mobile = mobile_entry_box.get()
            mail = mail_entry_box.get()
            gender = gender_entry_box.get()
            dob = dob_entry_box.get()
            addres = addres_entry_box.get()
            aadhar = aadhar_entry_box.get()
            nominame = nominame_entry_box.get()
            nomiaadhar = nomiaadhar_entry_box.get()
            nomimobile = nomimobile_entry_box.get()
            nomimail = nomimail_entry_box.get()
            branch = branch_entry_box.get()
            

            signup(name,fname,mname,mobile,mail,
                   gender,dob,addres,aadhar,nominame,nomiaadhar,nomimobile,nomimail,branch)

            mUsername_entry_box.delete('0','end')
            fUsername_entry_box.delete('0','end')
            Username_entry_box.delete('0','end')
            mobile_entry_box.delete('0','end')
            gender_entry_box.delete('0','end')
            mail_entry_box.delete('0','end')
            dob_entry_box.delete('0','end')
            addres_entry_box.delete('0','end')
            aadhar_entry_box.delete('0','end')
            nominame_entry_box.delete('0','end')
            nomiaadhar_entry_box.delete('0','end')
            nomimobile_entry_box.delete('0','end')
            nomimail_entry_box.delete('0','end')
            branch_entry_box.delete('0','end')

            controller.show_frame("CustSignupPage")


        signup_button = tk.Button(self, text='NEXT',
                                  font=('Times', 30, 'bold'),
                                  foreground='black',
                                  background='brown1',
                                  relief='raised',
                                  command=signup_command)
        signup_button.place(x=300,y=700)

# Define AboutPage window

class AboutPage(tk.Frame):
    def __init__(self,parent, controller):
        
        tk.Frame.__init__(self,parent,bg='lavender blush',height=1080,width=1920)
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times', 100, 'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        aboutlabel = tk.Label(self,
                                text="ABOUT US",
                                anchor='center',
                                font=('Times', 60, 'bold'),
                                foreground='crimson',
                                background='lavender blush')

        aboutlabel.place(x=600, y=150)

        '''infolabel = tk.Label(self,
                             text="FOR MORE DETAILS PLEASE CONTACT UNDERSIGNED\n\
Co-Founder and CEO Mr.Aditya Yadav\nPhone No. +91 9084830372 , 9897752324\
\nE-Mail:- adityashok989@gmail.com\n Address : O - 178 Pallav Puram Phase-\
2\n Modipuram Meerut Uttar Pradesh India  (250110)",
                            anchor='center',
                             font=('Times', 25, 'italic'),
                             foreground='red',
                             background='lavender blush')
        
        infolabel.place(x=50, y=550)'''


        madelabel = tk.Label(self,
                             text="MADE BY :-\nADITYA YADAV 23BCS10057  F\
ULL STACK DEVELOPER\nBRATISH \
DASGUPTA 23BCS10041  LITERATURE\nSAHIL NEHRA 23BCS10061  DESIGNER\nTANMAY SINGH 23BCS10799  LITERATURE\n\
KESHAV GOYAL 23BCS12036  DESIGNER",
                             anchor='center',
                             font=('Times', 40, 'italic'),
                             foreground='crimson',
                             background = 'lavender blush')
        
        madelabel.place(x=100, y=250)

        def login_exit():
            controller.show_frame("HomePage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=1000,y=650)

        def login_exit():
            controller.show_frame("MorePage")

        Start_page_button = tk.Button(self,
                                      text="BRANCHES",
                                      height=1,
                                      width=9,
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=400,y=650)

# Define Feedback Page Window

class FeedbackPage(tk.Frame):
    def __init__(self,parent, controller):
        
        tk.Frame.__init__(self,parent,bg='lavender blush',height=1080,width=1920)
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times', 100, 'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        feedlabel = tk.Label(self,
                                text="Feedback",
                                anchor='center',
                                font=('Times', 60, 'bold'),
                                foreground='black',
                                background='lavender blush')

        feedlabel.place(x=500, y=150)

        text = Text(self,
                    font=('Times', 30, 'bold'),
                    foreground='crimson',
                    height=7,
                    width=60,
                    background='white',)
        text.place(x=100,y=300)
        

        def submit():
            text.delete('1.0','end')
            controller.show_frame("HomePage")

        Start_page_button = tk.Button(self,
                                      text="SUBMIT",
                                      height=1,
                                      width=8,
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=submit)
        Start_page_button.place(x=350,y=650)

        def login_exit():
            text.delete('1.0','end')
            controller.show_frame("HomePage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=700,y=650)

# Define new page window

class MorePage(tk.Frame):
    def __init__(self,parent, controller):
        
        tk.Frame.__init__(self,parent,bg='lavender blush',height=1080,width=1920)
        
        self.controller = controller
        headinglabel = tk.Label(self,
                                text="Independent Bank",
                                anchor='center',
                                font=('Times', 100, 'bold'),
                                foreground='crimson',
                                background='lavender blush')

        headinglabel.place(x=250, y=0)

        '''infolabel = tk.Label(self,
                             text="FOR MORE DETAILS PLEASE CONTACT UNDERSIGNED\n\
Co-Founder and CEO Mr.Aditya Yadav\nPhone No. +91 9084830372 , 9897752324\
\nE-Mail:- adityashok989@gmail.com\n Address : O - 178 Pallav Puram Phase-\
2\n Modipuram Meerut Uttar Pradesh India  (250110)",
                            anchor='center',
                             font=('Times', 70, 'italic'),
                             foreground='black',
                             background='lavender blush')
        
        infolabel.place(x=50, y=200)'''

        infolabel = tk.Label(self,
                             text="BRANCHES",
                            anchor='center',
                             font=('Times', 70, 'bold'),
                             foreground='black',
                             background='lavender blush')
        
        infolabel.place(x=500, y=170)

        branches1label = tk.Label(self,
                             text="Meerut , Uttar Pradesh\
\n\nLucknow , Uttar Pradesh\
\n\nJind , Harayana\
\n\nJhunjhunu , Rajasthan\
\n\nBankura , West Bengal",
                            anchor='center',
                             font=('Times', 30, 'italic'),
                             foreground='brown1',
                             background='lavender blush')
        
        branches1label.place(x=200, y=300)

        branches2label = tk.Label(self,
                             text="Saharanpur , Uttar Pradesh\
\n\nBijnor , Uttar Pradesh\
\n\nRohtak , Harayana\
\n\nUttam Nagar , New Delhi\
\n\nKolkata , West Bengal",
                            anchor='center',
                             font=('Times', 30, 'italic'),
                             foreground='brown1',
                             background='lavender blush')
        
        branches2label.place(x=800, y=300)



        def login_exit():
            controller.show_frame("AboutPage")

        Start_page_button = tk.Button(self,
                                      text="CLOSE",
                                      height=1,
                                      width=6,
                                      font=('Times',30,'bold'),
                                      foreground='black',
                                      background='brown1',
                                      command=login_exit)
        Start_page_button.place(x=650,y=700)
        
# loop for showing window continously

if __name__ == '__main__':
    app = main_window()
    app.geometry('1920x1080')
    app.title('INDEPENDENT_BANK')
    app.mainloop()
