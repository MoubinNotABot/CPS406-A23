
from hmac import new
import pandas as pd 
import PySimpleGUI as sg
 
class Member:
    def __init__(self,fname, lname,phone,address,username,password):
     self.paid = False #boolean value, have they paid for the month?
     self.firstname = fname 
     self.lastname = lname
     self.phone = phone 
     self.address = address 
     self.username = ""
     self.password = "" 
     self.attendance = 0 #number of classes a member has attended in a 
     self.yearly = [] #list of boolean values to determine whether they have paid for each month in a year 
                      #e.g. [False,False,False] means they have not paid for the months of January,February and March 

    def resetpaid(self,begmonth):
        if begmonth == True:
            self.paid == False 
            self.yearly.append(True)
            return True
        else:
            return False 

    def getpaidstatus(self):
        return self.paid

    def getfirstname(self):
        return self.firstname 
    
    def getfirstname(self):
        return self.lastname 

    def getphonenumber(self):
        return self.phone

    def getaddress (self):
        return self.address

    def setusername(self,username):
        self.username = username 

    def setpassword(self,password):
        self.password = password 

    def checkusername(self):
        if self.username != "":
            return False
        else:
            return True 

    def checkpassword(self):
        if self.password != "":
            return False
        else:
            return True 

    def getusername(self):
        return self.username 

    def getpassword(self):
        return self.password  

    def incfrequency(self):
        self.frequency += + 1 

    def resetfrequency(self,begyear):
        if begyear == True:
            self.attendance = 0 
    
    def getattendance(self):
        return self.attendance

    def notpaid (self,endmonth):
        if (endmonth) and (self.getpaid == False):
            self.yearly.append(False)
    
    def paymentdiscountstatus(self): #return false if member hasn't paid for the last three months, true if they have 
        if len(self.yearly <= 3):
            return False 
        if len(self.yearly >= 3):
            for month in range (len(self.yearly)-3,len(self.yearly)):
                 if self.yearly[month] == True:
                     return True 
        return False

    def resetyearly(self,endyear):
        if endyear:
            self.yearly = []

    def resetattendance(self,begmonth):
        if begmonth: 
            self.attendance = 0 
    
    def numberofpayments(self):
        falsecount = 0 
        truecount = 0 
        for i in self.yearly:
            if self.yearly[i] == False:
                falsecount += 1
            elif self.yearly[i] == True:
                truecount += 1 
        return(truecount,falsecount,len(self.yearly))

    def updateframe(self,dataframe): #appending a new member to the final pandas datafrane 
        data = dataframe.append(dataframe)
        return dataframe 


def Login():
    usernames = list(data['Username'])
    passwords = list(data['Password'])
    username_layout = [[sg.Text('Enter Username')],
          [sg.Input()],
          [sg.Button('Enter'),sg.Exit()]]
    username_window = sg.Window('Login', username_layout)
    values1 = [0]
    if (values1[0] not in usernames):
        event, values = username_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
    while (values1[0] not in usernames):
        usernameerror_layout = [[sg.Text("Username not found, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
        usernameerror_window = sg.Window('Login', usernameerror_layout)
        event, values1 = usernameerror_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
    password_layout = [[sg.Text("Enter Password")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    password_window = sg.Window('Login', password_layout)
    values2 = [0]
    if (values2[0] not in passwords):
        event, values2 = password_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
    while (values2[0] not in passwords):
        passworderror_layout = [[sg.Text("Password not found, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
        passworderror_window = sg.Window('Login', passworderror_layout)
        event, values = passworderror_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 

def Register():
    register_layout =   [[sg.Text("Enter First Name")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values3= [0]
    while True: 
        event, values3 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        else:
            firstname = values3[0] 
        break 

    register_layout =   [[sg.Text("Enter Last Name")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values4= []
    while True: 
        event, values4 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        lastname = values4[0] 
        break 
    
    register_layout =   [[sg.Text("Enter phone number")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values5= [0]
    while True: 
        event, values5 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        phone = values5[0]
        break 


    register_layout =   [[sg.Text("Enter address")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values6= [0]
    while True: 
        event, values6 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        address  = values6[0]
        break 
        
    register_layout =   [[sg.Text("Enter username")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values7= [0]
    while True: 
        event, values7 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        username  = values7[0]
        break 

    register_layout =   [[sg.Text("Enter password")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values8= [0]
    while True: 
        event, values8 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        password  = values8[0]
        break 
    temp =  Member(firstname,lastname,phone,address,username,password)
    temp_df = pd.DataFrame({'First Name':[firstname], 'Last Name': [lastname], 'Phone': [phone], 'Address': [address], 'Username': [username], 'Password':[password]})
    data = temp.updateframe(temp_df)
    print(data)

    return True 


data = pd.DataFrame() 
sg.theme('Dark Blue 3')  

    
values1=[0]
layout1 = [[sg.Text('Choose whether to login or register as a club member')],
          [sg.Button('Login'), sg.Button('Register'),sg.Exit()]]

window1 = sg.Window('Salsa Dancing 101', layout1)
while True:
    event, values = window1.read()
    if event == "Register":
        Register()
        break 
    elif  event == "Login":
        Login()
        break 
    elif (event == sg.WIN_CLOSED) or (event == 'Exit'):
        break
window1.close()






    


    



