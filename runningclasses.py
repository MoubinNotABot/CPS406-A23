from hmac import new
import pandas as pd 
import PySimpleGUI as sg
from  member import Member
from IncomeStatement import IncomeStatement 
import os 
sg.theme('Dark Blue 3')  


'''
need to load the proper data before we run the user interface 
'''

<<<<<<< HEAD
member_path = 'C:\\Users\\tahmi\\Documents\\GitHub\\CPS406-A23\\allmembers.csv' #local path where .csv file containing all member data will be saved 
=======
member_path = './allmembers.csv' #local path where .csv file containing all member data will be saved 
>>>>>>> b5a99f70b224b6b5191cbe69e6f24df98ff7a225
if os.path.isfile(member_path): #if there is already a file, load that file 
    member_data = pd.read_csv('allmembers.csv',index_col=[0])
else: #othwerise create a new csv file (in the format needed for the member database) and load that file 
    member_data = pd.DataFrame(columns = ['Type', 'First Name', 'Last Name', 'Phone', 'Address', 'Username', 'Password','self_paid','self_attendance','self_weekspaid','self_penalty','self_balance', 'discount_count'])
    member_data.to_csv('allmembers.csv')
    member_data = pd.read_csv('allmembers.csv',index_col=[0])

IncomeStatement = IncomeStatement() #create a new income state class to keep track of profits, expenses and debt 

def importdataframe(dataframe): #this function takes the dataframe containing member information and creates  a lsit of all members so that important attributes can be 
    #changed/tracked 
    global master_list
    master_list = []
    for row in range (0,dataframe.shape[0]):
        newmember = Member(dataframe.iloc[row]['Type'], dataframe.iloc[row]['First Name'],dataframe.iloc[row]['Last Name'],dataframe.iloc[row]['Phone'],dataframe.iloc[row]['Address'],dataframe.iloc[row]['Username'],
        dataframe.iloc[row]['Password'], dataframe.iloc[row]['self_paid'], dataframe.iloc[row]['self_attendance'], dataframe.iloc[row]['self_weekspaid'],dataframe.iloc[row]['self_penalty'],dataframe.iloc[row]['self_balance'],dataframe.iloc[row]['discount_count'])
        master_list.append(newmember)
    return master_list

<<<<<<< HEAD
importdataframe(member_data)
=======
importdataframe(member_data) 
for i in master_list:
    print(i.balance)

>>>>>>> b5a99f70b224b6b5191cbe69e6f24df98ff7a225
def Login(): #checks whether member username and password is correct when user logs in, based on the type of user (trasurer,member, coach) the interface will be different 
    global member_data
    member_usernames = list(member_data['Username']) 
    member_passwords = list(member_data['Password']) 
    master_list = importdataframe(member_data)
    
    values1=[0]
    username_layout = [[sg.Text('Enter Username')],
          [sg.Input()],
          [sg.Button('Enter'),sg.Exit()]]
    username_window = sg.Window('Login', username_layout)
    event, values1 = username_window.read()
    while (values1[0] not in member_usernames):
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            username_window.close() 
            return None 
        else: 
            usernameerror_layout = [[sg.Text("Username not found, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
            usernameerror_window = sg.Window('Login', usernameerror_layout)
            event, values1 = usernameerror_window.read()
    if values1[0]  in member_usernames:
        username_window.close()
    correct_username = values1[0]
    password_layout = [[sg.Text("Enter Password")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
    password_window = sg.Window('Login', password_layout)
    event, values2 = password_window.read()
    while (values2[0] not in member_passwords):
        passworderror_layout = [[sg.Text("Password not found, try again")],[sg.Input()], [sg.Button("Enter"),sg.Exit()]]
        passworderror_window = sg.Window('Login', passworderror_layout)
        event, values = passworderror_window.read()
        if (event == sg.WIN_CLOSED) or (event == 'Exit'):
            passworderror_window .close() 
            return None 
    if (values2[0]  in member_passwords):
           password_window.close()



    ''' Need GUI here so that when members login, they can register for all classes running that month'''
    for person in master_list:
        if person.username == correct_username:
            correct_type = person.type 
    if correct_type.lower() == 'member':
        memberlogin(correct_username) #call member interface if user is a member 
    elif correct_type.lower() == 'coach':
        coachlogin() #call coach interface if user is a coach 
    elif correct_type.lower() == 'treasurer': 
        treasurerlogin() #call treasurer interface if users is a treasurer 
    return None 



def Register(): #allows users to register a coach, member or treasurer 
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
    temp =  Member(type.lower(), firstname,lastname,phone,address,username,password,False,0,0,0,0,0)
    temp_df = pd.DataFrame({'Type': type.lower(),'First Name':[firstname], 'Last Name': [lastname], 'Phone': [phone], 'Address': [address], 'Username': [username], 'Password':[password], 
    'self_paid':[temp.paid],'self_attendance': [temp.attendance], 'self_weekspaid':[temp.weekspaid], 'self_penalty':[temp.penalty],'self_balance':[temp.balance],'discount_count':[temp.discountCount]  }) #create a temp_df for the new member that has been created 
    member_data = member_data.append(temp_df) #temp_df is a dataframe with one row, append this row from the data frame to the master data frame being used to track all members 
    member_data.to_csv('allmembers.csv')
    return None  
def scheduleUI(): #function for the schedule GUI
    layout=[[sg.Text('Schedule an appointment',size=(20, 1),justification='left')],
        [sg.Combo(['April 7th','April 14th','April 21st', 'April 28th',],default_value='April 7th',key='board')],
        [sg.Button('Proceed with payment',),sg.Button('CANCEL',)]]
    win =sg.Window('Schedule',layout)
    while True:
        e,v=win.read()
        print(e,v)
        if e == sg.WIN_CLOSED or e == 'CANCEL':
                break
        elif e== 'Proceed with payment':
                payment_normal()

    win.close()

def generateattendancelist(master_list): #use this function to generate an attendance list for a class 
    attendance_list = []
    for i in range(0,1):
        attendee = master_list[i]
        attendance_list.append(attendee)
    return attendance_list 
        
#show drop down class for every 7 days (show whole month... 4 classes)
# after a user schedules a class, automatically go to a payment window if self.paid == False 
# once user enters credit card, increment self.balance by 10 and incr. self.weekspaid by 1 

def notifymembersofpenalty(penaltylist):
    notifylist = []
    for i in penaltylist:
        notifylist.append(i.firstname)
    notify_layout = [[sg.Listbox(
            values=notifylist, enable_events=True, size=(40, 20),
        )]]
    notify_layout2 = [[sg.Text("Please note you have a negative balance after your last class. \nMake a payment to resolve your debts.")],[sg.Button('Send Text')]]
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

attendance = generateattendancelist(master_list)

def removemembers(alist): #because the user has a penalty, no longer eligible to be in the club. Remove from main dataframe. 
    global member_data 
    droplist = []
    for i in alist:
        droplist.append(i.firstname)
        
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
    elif (event == 'Drop Members'):
        for classattendee in alist: 
            for onemember in maindf:
                if classattendee.username == onemember.username:
                     maindf =  member_data.drop()
    return None

def runclass(attendancelist): #paramater attendancelist: some kind of attendance list after a class submitted by a coach 
    notifylist = [] # list of all members that need to be notified of a skipped payment 
    droplist = [] #list of all members that need to be drooped from main database because of two skipped payments 
    revenueamount = 0 #calcules how many people attended AND PAID for the class a
    for person in attendancelist: 
        if (person.balance < 10) and (person.paid == False): #let's say class is $10, if balance is less than $10  and haven't paid for month-> debt 
            person.penalty +=1  #flag that this person is in debt 
            if person.penalty == 1: #if the person only has one penalty of 1, the just need to be notified 
                notifylist.append(person)
                notifymembersofpenalty(notifylist) #  function to notify members in the penalty list 
            elif person.penalty >=2:
                droplist.append(person) #function to drop members who have skipped payment more than once 
        elif (person.balance < 10) and (person.paid == False):
            revenueamount += 10 
        person.balance = person.balance - 10 
        person.attendance = person.attendance + 1 
        IncomeStatement.addtorevenue(revenueamount) #revenue from classes is updated in the Income Statement 

    
        # if person.paid == False: #if the person does not pay by month...
        #     person.balance = person.balance - 10 # subtract $10 off balance to pay for class 
        # if person.discountstatus(): 
        #     person.balance = person.balance - 9 #10% off the class  
    if len(droplist)>=1:
        removemembers(droplist) #function to drop all members who have missed more than two payments 
    
    return None         
runclass(attendance)


#removemembers(['Rachita'])

#notifymembersofpenalty(['Rachita'])

# def notifymembersofclass(memberlist):
#     notifylist = memberlist 
#     notify_layout = [[sg.Listbox(
#             values=notifylist, enable_events=True, size=(40, 20),
#         )]]
#     notify_layout2 = [[sg.Text("Only two days left before our class this week! If you plan on attending, make sure to register.")],[sg.Button('Send Text')]]
#     notify_layout_final = [
#     [
#         sg.Column(notify_layout),
#         sg.VSeperator(),
#         sg.Column(notify_layout2),
#     ]
#     ]
#     notify_window = sg.Window('Class Notification', notify_layout_final)
#     event, values = notify_window.read()
#     if (event == sg.WIN_CLOSED) or (event == 'Exit') or (event == 'Send Text'):
#         notify_window.close()
#     return None
# notifymembersofclass['Rachita'])

def futureclasses(attendance_list):   #notify all members about changes or details about future practices.
    notifylist = attendance_list
    notify_layout = [[sg.Listbox(
            values=notifylist, enable_events=True, size=(40, 20),
        )]]
    notify_layout2 = [[sg.Text("Enter a message to notify members with details about future classes or if any changes are made to practices. \n")],
                      [sg.Input()], [sg.Button('Send Message')]]
    notify_layout_final = [
    [
        sg.Column(notify_layout),
        sg.VSeperator(),
        sg.Column(notify_layout2),
    ]
    ]
    notify_window = sg.Window('Future and/or Changes to Practises', notify_layout_final)
    event, values = notify_window.read()
    if (event == sg.WIN_CLOSED) or (event == 'Exit') or (event == 'Send Message'):
        notify_window.close()
    return None
#futureclasses(['Rachita'])
    
    
def memberlogin(username): #use this function to let members schedule and pay for a class 
    layout_member = [[sg.Text('Choose whether to sign up for a class or make a payment')],
          [sg.Button('Schedule Class'), sg.Button('Make Payment'),sg.Button('Exit')]]
    member_window = sg.Window('Welcome', layout_member) 
    while True:
        event,values=member_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Schedule Class':
            layout=[[sg.Text('Schedule an appointment',size=(20, 1),justification='left')],
                    [sg.Combo(['April 7th','April 14th','April 21st', 'April 28th',],default_value='April 7th',key='board')],
                    [sg.Button('Proceed with payment',),sg.Button('CANCEL',)]]
            win =sg.Window('Schedule',layout)

            while True:
                event,values = win.read()
                if event == 'CANCEL' or event == sg.WIN_CLOSED:
                    break
                if event == 'Proceed with payment':
                    layout = [[sg.Text('Each class costs 10 dollars and monthly payments cost 40 dollars')],
                              [sg.Text('Enter Credit Card Number')],
                              [sg.Input('', enable_events=True,  key='-INPUT-')],
                              [sg.Text('Enter Secuirity Code')],
                              [sg.Input('', enable_events=True,  key='-INPUT2-')],
                              [sg.Text('Enter Expiration Date')],
                              [sg.Input('', enable_events=True, key='-INPUT3-')],
                              [sg.Button('Pay per class'), sg.Button('Pay for month'), sg.Button('Exit')]]
                    window=sg.Window('Payment Information',layout)

                    while True:
                        event1,values1=window.read()
                        if event1 == 'Exit' or event1 == sg.WIN_CLOSED:
                            break
                        elif event1 == 'Pay for month':
                            sg.Popup('You have successfully paid for the month')
                            for i in master_list:
                                if (i.username==username):
                                    i.paid=True
                            member_data.loc[member_data['Username']==username, ['self_paid']]=True
                            print (member_data)
                        elif event1 == 'Pay per class':
                            sg.Popup('You have successfully paid for the class')
                            for i in master_list:
                                if(i.username==username):
                                    i.balance+=10

                    window.close()
                win.close()
            member_window.close()
        #need functionality: if person has paid payments for the month, self.paid = True 
        #otherwise incremement self.balance by 10 
    return None 
def coachlogin(): #coach to choose wheter to run a class and submit attednance, modify member list(to dop members), send text for reminders and notifications  
    coachlayout = [[sg.Text('Do you want to submit attendance for a class?')],
          [sg.Button('Submit Attendance'),sg.Exit()]]
    coach_window = sg.Window('Coach Login', coachlayout)
    event, values = coach_window.read()
    if event == "Submit Attendance":    #Moubin attendance function here 
        master_list = importdataframe(member_data)
        attendance_list = generateattendancelist(master_list) #when user submits attendance list 
        runclass(attendance_list) #user can drop members after submitting an attendance list for a class 
    
    futureclasses(master_list) #send text for reminders 
    return None 

def treasurerlogin(): #check income statement to date, manage coach list and schedule 
    treasurerlayout = [[sg.Text('Choose whether to manage coach list or check financials')],
        [sg.Button('Manage Coach List'), sg.Button('Check Financials'),sg.Button('Log out')]]
    treasurer_window = sg.Window('Treasurer Login', treasurerlayout)
    event, values =  treasurer_window.read()
    while (event != "Log out") and (event != sg.WIN_CLOSED): 
        if event == "Manage Coach List": 
            count = 0  #for any given month, count how many times in the month coach has run a class, pay coach based on this number
            coachattendancelayout = [[sg.Text('Confirm coach attendance')],
            [sg.Checkbox('Jan 7', size=(12, 1), default=False),],
            [sg.Checkbox('Jan 14', size=(12, 1), default=False),],
            [sg.Checkbox('Jan 21', size=(12, 1), default=False),],
            [sg.Checkbox('Jan 28', size=(12, 1), default=False),],
            [sg.Button('Submit')]]
            coachattendancewindow = sg.Window('Manage Coach List', coachattendancelayout)    
            event, values = coachattendancewindow.read()
            if event == 'Submit': #once treasurer submits checklist with dates for coach attendance, check which boxes have been selected as "True" since these are the dates the coach has attednance 
                for i in values.values():
                    if i == True:
                        count = count + 1 
                        IncomeStatement.updatecoachexpense(count) #add this to list of expenses for coach
                        coachattendancewindow.close()
        elif event == "Check Financials": #if user wants to check financials, display the income state to date 
            financelayout = [[sg.Text('Choose whether to see income statement, see profits, see debts, or pay rent, or close entries for the month')],
            [sg.Button('See Income Statement'), sg.Button('See Profits'),sg.Button('See Debts'),sg.Button('Pay Rent'),sg.Button('Pay Coach'),sg.Button('Close Entries')]]
            financials_window = sg.Window('Check Financials', financelayout)
            event, values = financials_window.read()
            while event != sg.WIN_CLOSED: 
                if event == "See Income Statement":
                    IncomeStatement.updateAP(importdataframe(member_data))
                    IncomeStatement.UI()
                elif event == 'See Profits':
                    IncomeStatement.seeprofits()
                elif event == 'See Debts':
                    IncomeStatement.seedebts()
                elif event == 'Pay Rent':
                    IncomeStatement.payrent()
                elif event == 'Pay Coach':
                    IncomeStatement.paycoach()
                elif event == 'Close Entries':
                    IncomeStatement.closemonth(True)
                event, values = financials_window.read()
            if (event == sg.WIN_CLOSED):
                financials_window.close()
                
        #treasurer_window = sg.Window('Treasurer Login', layout1)
        event, values =  treasurer_window.read()

    if (event == "Log out"):
        treasurer_window.close()
        displaymain()
    if (event == sg.WIN_CLOSED):
        treasurer_window.close()

    return None 

def displaymain():
    layout1 = [[sg.Text('Choose whether to login or register as a club member')],
        [sg.Button('Log in'), sg.Button('Register'),sg.Exit()]]
    window1 = sg.Window('Salsa Dancing 101', layout1)
    event, values = window1.read()
    if event == "Register":
            Register()
    elif  event == "Log in":
            Login()
    window1.close()
    return None 
displaymain()
    

