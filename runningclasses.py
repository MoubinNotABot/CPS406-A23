from hmac import new
import pandas as pd 
import PySimpleGUI as sg
from  member import Member
import os 
sg.theme('Dark Blue 3')  


#let's say classes run every Tuesday of the month, need interface which allows a member to register for a class 
#for each class, need a list of all members that have attended that class 
#check that list to see if the members have paid in advance for that month, or paid for that class as a one-time fee 
#if not, add to a list of members who have not paid 

member_path = '/Users/rachitasingh/Desktop/CPS 406 Software Engineering/allmembers.csv' 
if os.path.isfile(member_path):
    member_data = pd.read_csv('allmembers.csv',index_col=[0])
else:
    member_data = pd.DataFrame(columns = ['Type', 'First Name', 'Last Name', 'Phone', 'Address', 'Username', 'Password','self_paid','self_attendance','self_weekspaid','self_penalty','self_balance'])
    member_data.to_csv('allmembers.csv')
    member_data = pd.read_csv('allmembers.csv',index_col=[0])




def Login():
    global member_data
    member_usernames = list(member_data['Username']) 
    member_passwords = list(member_data['Password']) 
    username_layout = [[sg.Text('Enter Username')],
          [sg.Input()],
          [sg.Button('Enter'),sg.Exit()]]
    username_window = sg.Window('Login', username_layout)
    event, values1 = username_window.read()
    if (event == sg.WIN_CLOSED) or (event == 'Exit'):
        return None 
    while (values1[0] not in member_usernames):
        usernameerror_layout = [[sg.Text("Username not found, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
        usernameerror_window = sg.Window('Login', usernameerror_layout)
        event, values1 = usernameerror_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
    correct_username = values1[0]
    
    password_layout = [[sg.Text("Enter Password")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    password_window = sg.Window('Login', password_layout)
    event, values2 = password_window.read()
    if (event == sg.WIN_CLOSED) or (event == 'Exit'):
        return None 
    while (values2[0] not in member_passwords):
        passworderror_layout = [[sg.Text("Password not found, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
        passworderror_window = sg.Window('Login', passworderror_layout)
        event, values = passworderror_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 

    ''' Need GUI here so that when members login, they can register for all classes running that month'''
    memberlogin()
    coachlogin()
    treasurer()

    layout_member = [[sg.Text('Choose whether to sign up for a class or make a payment')],
          [sg.Button('Schedule Class'), sg.Button('Make Payment'),sg.Exit()]]
    member_window = sg.Window('Welcome', layout_member)
    event, choice = member_window.read()
    if event == "Make Payment":
            payment_layout =   [[sg.Text("Enter Credit Card")],[sg.Input()], [sg.Text("Enter Security code")],[sg.Input()], [sg.Text("Enter Payment Amount")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
            payment_window = sg.Window('Make Payment', payment_layout)
            event, paymentinput = payment_window.read()
            for member in master_list:
                if correct_username == member.username:
                    member.balance = int(paymentinput[2])
                    print (member.balance)
    

def Register():
    global member_data
    global coach_data
    global treasurer_data
    member_usernames = list(member_data['Username']) 
    register_layout =   [[sg.Text("Enter role(coach,member,treasurer)")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    valuesx= [0]
    while True: 
        event, valuesx = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        else:
            type = valuesx[0] 
        break 
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
    event, values7 = register_window.read()
    if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
    while (values7[0]  in member_usernames):
            usernametaken_layout = [[sg.Text("Username already used, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
            usernametaken_window = sg.Window('Register', usernametaken_layout)
            event, values7 = usernametaken_window.read()
            if (event == sg.WIN_CLOSED) or (event == 'Exit'):
                break  
    if (values7[0] not in member_usernames):
            username = values7[0]
    register_layout =   [[sg.Text("Enter password")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    register_window = sg.Window('Register', register_layout)
    values8= [0]
    while True: 
        event, values8 = register_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            return None 
        password  = values8[0]
        break 
    temp =  Member(type.tolower(), firstname,lastname,phone,address,username,password,False,0,0,0,0)
    temp_df = pd.DataFrame({'Type': type.tolower(),'First Name':[firstname], 'Last Name': [lastname], 'Phone': [phone], 'Address': [address], 'Username': [username], 'Password':[password], 
    'self_paid':[temp.paid],'self_attendance': [temp.attendance], 'self_weekspaid':[temp.weekspaid], 'self_penalty':[temp.penalty],'self_balance':[temp.balance] })
    member_data = member_data.append(temp_df) #temp_df is a dataframe with one row, append this data fram to the master data frame 
    member_data.to_csv('allmembers.csv')
    return True 


values1=[0]
layout1 = [[sg.Text('Choose whether to login or register as a club member')],
        [sg.Button('Login'), sg.Button('Register'),sg.Exit()]]
window1 = sg.Window('Salsa Dancing 101', layout1)
event, values = window1.read()
if event == "Register":
        Register()
elif  event == "Login":
        Login()
window1.close()

#let's say classes run every Tuesday of the month, need interface which allows a member to register for a class 
#for each class, need a list of all members that have attended that class 
#check that list to see if the members have paid in advance for that month, or paid for that class as a one-time fee 
#if not, add to a list of members who have not paid 


def importdataframe(dataframe):
    master_list = []
    for row in range (0,dataframe.shape[0]):
        newmember = Member(dataframe.iloc[row]['Type'], dataframe.iloc[row]['First Name'],dataframe.iloc[row]['Last Name'],dataframe.iloc[row]['Phone'],dataframe.iloc[row]['Address'],dataframe.iloc[row]['Username'],
        dataframe.iloc[row]['Password'], dataframe.iloc[row]['self_paid'], dataframe.iloc[row]['self_attendance'], dataframe.iloc[row]['self_weekspaid'],dataframe.iloc[row]['self_penalty'],dataframe.iloc[row]['self_balance'])
        master_list.append(newmember)
    return master_list 


master_list = importdataframe(member_data)
def generateattendancelist(master_list):
    attendance_list = []
    for i in range(0,3):
        attendance_list.append(i)
    return attendance_list 

attendance_list = generateattendancelist(master_list) 
        
#show drop down class for every 7 days (show whole month... 4 classes)
# after a user schedules a class, automatically go to a payment window if self.paid == False 
# once user enters credit card, increment self.balance by 10 and incr. self.weekspaid by 1 



def runclass(attendancelist): #some kind of attendance list after a class submitted by a coach 
    notifylist = []
    droplist = []
    for person in attendancelist: 
        if (person.balance < 10) and (person.paid == False): #let's say class is $10, if balance is less than $10  and haven't paid for month-> debt 
            person.penalty +=1  #flag that this person is in debt 
            person.balance = person.balance - 10 #implemented a $2 penality if a person has skipped a class more than once 
            if person.penalty <2:
                notifylist.append(person)
                notifymembers(notifylist) # create function to notify members in the penalty list who 
            elif person.penalty >=2:
                droplist.append(person)
        # if person.paid == False: #if the person does not pay by month...
        #     person.balance = person.balance - 10 # subtract $10 off balance to pay for class 
        # if person.discountstatus(): 
        #     person.balance = person.balance - 9 #10% off the class  
    if len(droplist)>=1:
        removemembers(droplist)
    
runclass(attendance_list)
        


def removemembers(alist): #because the user has a penalty, no longer eligible to be in the club. Remove from main dataframe. 
    global member_data 
    maindataframe = importdataframe(member_data)
    droplist = alist
    drop_layout = [[sg.Listbox(
            values=droplist, enable_events=True, size=(40, 20),
        )], [sg.Button('Drop Members')]]
    drop_layout_final = [
    [
        sg.Column(drop_layout),
    ]
    ]
    drop_window = sg.Window('Drop Members', drop_layout_final)
    event, values = drop_window.read()
    if (event == sg.WIN_CLOSED) or (event == 'Exit') or (event == 'Drop Members'):
        drop_window.close()
    for classattendee in alist: 
        for onemember in maindf:
            if classattendee.username == onemember.username:
                maindf =  maindataframe.drop()



    return None

def notifymembers(penaltylist):
    notifylist = penaltylist
    notify_layout = [[sg.Listbox(
            values=notifylist, enable_events=True, size=(40, 20),
        )]]
    notify_layout2 = [[sg.Text("Please note you have a negative balance after your list class. \nMake a payment to resolve your debts")],[sg.Button('Send Text')]]
    notify_layout_final = [
    [
        sg.Column(notify_layout),
        sg.VSeperator(),
        sg.Column(notify_layout2),
    ]
    ]
    notify_window = sg.Window('Skipped Payments', notify_layout_final)
    event, values = notify_window.read()
    if (event == sg.WIN_CLOSED) or (event == 'Exit') or (event == 'Send Text'):
        notify_window.close()
    return None



    


