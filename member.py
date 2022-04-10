
from hmac import new
import pandas as pd 
import PySimpleGUI as sg
import os 



 
class Member:
    def __init__(self,type,fname, lname,phone,address,username,password,paid,attendance,weekspaid,penalty,balance):
     self.type = type #string value representing whether member is a coach, treasurer or attendee 
     self.firstname = fname 
     self.lastname = lname
     self.phone = phone 
     self.address = address 
     self.username = username #username and password will be created upon registration 
     self.password = password
     self.paid = paid #boolean value, have they paid for the MONTH 
     self.attendance = attendance#number of classes a member has attended in a YEAR 
     self.weekspaid = weekspaid  #list of boolean values to determine whether they have paid for each month in a year
                            #e.g. [False,False,False] means they have not paid for the months of January,February and March 
                            #initially all months will be False 
     self.penalty = penalty #if member has skipped a payment (either not paid in advance for the month or not paid for a class), raise this flag to true 
     self.balance = balance #keeps track of any payments a member has made for each class (if they choose not to pay for the month)
                            #increment this every time a member pays for a class 

    def resetmonth(self,begmonth): #begmonth is a boolean value to determine whether it is the beginning of the month when the function resetpaid() is called
        if begmonth == True:
            self.paid == False #reset self.paid var, will be false unless monthpaid() function is used to set to true 


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

    def getusername(self):
        return self.username 

    def getpassword(self):
        return self.password  

    def getattendance(self):
        return self.attendance

    def getweekpaid(self):
        return self.weekpaid

    def incattendance(self): #increase the attendance count by 1 (this happens when member has attended a class)
        self.attendance += + 1 
    
    def paidformonth(self):
        self.weekspaid += 4 
        self.paid = True 
    
    def paidforclass(self):
        self.weekspaid += 1 

    def discountstatus(self): #makes a class $9 rather than $10 if member has paid for 12 weeks and has not taken a class without paying 
        if (self.weekspaid >= 12) and (self.penalty ==0):
            return True             
        return False 

    def addpenalty(self): #add a $2 penalty if a member has taken a class without paying 
        if (self.penalty > 0):
            return True             
        return False 

    def resetyear(self,endyear):
        if endyear:
            self.yearly = [False] *12 #self.yearly keep tracks of whether the member has paid in advance for the month, for each month of the year 
                                      #reset this var at the beginning of each eay 
            self.attendance = 0 #self.attendance keeps track of number attendances for the year, reset this var at the beginning of each year 


    def updateframe(self,dataframe): #anytime a new member registers, appending the new member to the final pandas datafrane which contains all data frames
        data = dataframe.append(dataframe)
        return dataframe 


