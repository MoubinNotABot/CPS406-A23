import pandas as pd 
import copy
from random import randrange
from turtle import ScrolledCanvas, color
import PySimpleGUI as sg
import tkinter
from member import Member

members = []

for i in range(20):
    member = Member("member",str(i*100),str(i*i), randrange(0,10)*randrange(0,10),"home"+str(i),"u"+str(i),
    "password", False, randrange(0,10)*randrange(0,10),randrange(0,20),0,randrange(0,10)*randrange(0,10),0)
    member.attendance = randrange(0,10) # assigning random attendance
    members.append(member)


def sortByPaidStreak(array): # high to low. can modify this to be by attendance or days paid or not.
    sortedArr = copy.deepcopy(array)
    n = len(sortedArr)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if sortedArr[j].weekspaid < sortedArr[j + 1].weekspaid:
                sortedArr[j], sortedArr[j + 1] = sortedArr[j + 1], sortedArr[j] #swap
                already_sorted = False
        if already_sorted:
            break
    return sortedArr


def sortByAttendance(array): # high to low. can modify this to be by attendance or days paid or not.
    sortedArr = copy.deepcopy(array)
    n = len(sortedArr)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if sortedArr[j].attendance < sortedArr[j + 1].attendance:
                sortedArr[j], sortedArr[j + 1] = sortedArr[j + 1], sortedArr[j] #swap
                already_sorted = False
        if already_sorted:
            break
    return sortedArr


def format(string, cond): # used to align and color the member listing
    string = str(string)
    newString = string + " " * (25 - len(string)) 
    if cond:
        return sg.Text(newString, font = "TkFixedFont", background_color="DarkGreen") 
    return sg.Text(newString, font = "TkFixedFont")

def showListing(membersArr): # given an array, make a window out of it.
    col = [ # the part of the col that does not change.
        [
        sg.Text("                                                                                                                "), # space between button and border
        sg.Button("Sort by attendance"),
        sg.Text("            "), # space between buttons
        sg.Button("Sort by payment")],
        [
        sg.Text("Number               ", font="TkFixedFont 15 bold"), 
        sg.Text("Name                    ", font="TkFixedFont 15 bold"), 
        sg.Text("Classes attended", font="TkFixedFont 15 bold"), 
        sg.Text("Payments made  ", font="TkFixedFont 15 bold"),
        sg.Text("Phone number      ", font="TkFixedFont 15 bold"), 
        sg.Text("Address          ", font="TkFixedFont 15 bold"),
        ]
        ]

    # add to col
    number = 1
    for i in membersArr:
        
        cond = i.discountstatus() or hasAttendanceDiscount(i) # this desides weather or not a member will be colored

        col.append([
            format(str(number), cond),
            format(i.firstname+" "+i.lastname, cond),
            format(i.attendance, cond),
            format(""+str(i.weekspaid), cond), # replace with paidStreak
            format(""+str(i.phone), cond),
            format(""+i.address, cond)
        ]) # adding a row
        number += 1
    
    # displaying the col.
    listingLayout = [[sg.Column(col, scrollable=True, vertical_scroll_only=True, size = (1920,1080))]]
    listingWindow = sg.Window("Member Listing", listingLayout, size=(1920, 1080))
    
    # add functionality to the buttons. 
    while True:
        event, values = listingWindow.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "Sort by attendance":
            showListing(sortByAttendance(membersArr))
            break # closing one window, will close all the windows. 

        if event == "Sort by payment":
            showListing(sortByPaidStreak(membersArr))
            break # closing one window, will close all the windows. 

    listingWindow.close() # close the window


def topN (array, n): # for the top 10
    return array[0:n]

#given a members array, reset the database to hold what is there
def exportToDataBase(memberArr):
    """
    why do i need this?
    person properties such as penalty are not consistent with the database
    """
    # clear database
    member_data = pd.DataFrame(
        columns = ['Type', 'First Name', 'Last Name', 
        'Phone', 'Address', 'Username', 'Password','self_paid',
        'self_attendance','self_weekspaid','self_penalty','self_balance', 'discount_count'])
    
    # adding each member into the "new" database 
    for temp in memberArr:
        temp_df = pd.DataFrame(
            {'Type': temp.type.lower(),'First Name':[temp.firstname], 
            'Last Name': [temp.lastname], 'Phone': [temp.phone], 'Address': [temp.address], 
            'Username': [temp.username], 'Password':[temp.password], 
            'self_paid':[temp.paid],'self_attendance': [temp.attendance], 
            'self_weekspaid':[temp.weekspaid], 'self_penalty':[temp.penalty],
            'self_balance':[temp.balance],
            'discount_count':[temp.discountCount]
            }
            )
        member_data = member_data.append(temp_df)
    member_data.to_csv('allmembers.csv')

def resetAttDiscount(member):
    if member.discountstatus(): # if member has payment discount, and if has 2 discounts, reset it.
        if member.discountCount == 2:
            member.discountCount = 1
    elif member.discountCount == 1: # if member has no payment discount but discount atr is 1, set it to 0
        member.discountCount = 0


def hasAttendanceDiscount(member): 
    resetAttDiscount(member) # reset attendance discount
    topTen = topN(sortByAttendance(members),10)
    topTenUsername = []
    for person in topTen:
        topTenUsername.append(person.username)
    if member.username in topTenUsername:
        member.discountCount += 1
        return True
    return False

def makeAttendance(): # the ui to get an array of usernames.
    layout = [
        [sg.Text("Please write the names of those who attended today's class")],
        [sg.Multiline(size=(50,50))],
        [sg.Button("Submit")]
    ]
    window = sg.Window("Attendance", layout, size=(1920,1080))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return []
        if event == "Submit":
            break
    string = values[0]
    window.close()
    return string.split("\n")

def toPerson(arr): # takes in an array of usernames made by the admin
    returnArr = []
    for username in arr:
        for person in members:
            if person.getusername() == username:
                returnArr.append(person)
    return returnArr


def printer(members): # 
    for i in range(len(members)):
        print(members[i].username)
printer(members)

def test(membersArr):
    print("in test")
    print("out test")

print("##################################")
# attendance = toPerson(makeAttendance())
# printer(attendance)
# for i in attendance:
#     print(i.firstname, i.attendance, i.discountCount)

exportToDataBase(members)
# def test():
    # # for i in range(10):
    # #     print(i)
    # print("loDFl".lower())

# test(members)

# showListing(members)








'''
discount attribute? 0,1,2. number of discounts a member has...
reset attendance discount? like if not the top10, then attendance discount will be removed...
but also need to make sure that we are not taking away the other discount in the process
goes through every member, resets it.
done as the initialization for has
if has other discount:
    if discount count == 2:
        discount count -= 1
    if discount count == 1:
        pass
else:
    if discount count == 1:
        discount -= 1    

'''