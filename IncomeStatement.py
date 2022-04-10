import PySimpleGUI as sg

rent = 500 


sg.theme('Dark Blue 3')  # please make your windows colorful


class IncomeStatement: 
    def __init__(self):
        self.revenue = {'Classes': 0}
        self.expenses = {'Coach': 0, 'Rent':0}
        self.log = []
        self.monthlyAP = 0
        self.rentdebt = []
        self.unpaidcoach = []
    
    def getrevenue(self):
        return self.revenue 

    def getrevenue(self):
        return self.revenue 
    
    def getlog(self):
        return self.log 

    def getAP(self):
        return self.monthlyAP
    

    def getrentdebt(self):
        return self.rentdebt

    def getunpaidcoach(self):
        return self.unpaidcoach

    def resetyear(self,newyear):
        if newyear == True: 
             self.revenue ['Classes'] = 0 #revenue comes from class payments 
             self.expenses['Coach'] = 0 #paying the coach is an expense 
             self.expenses['Rent'] = 0 #paying rent is an expense 
             self.log = []
             self.monthlyAP = 0
             self.rentdebt = []
             self.unpaidcoach = [] 
    
    # def runclass(self,number_of_attendees,class_price,classended):
    #     if classended == True: 
    #         self.revenue['Class'] += number_of_attendees * class_price
    
    def addtorevenue(self, amount): #anytime someone makes a payment, add to revenue generated from classes 
        self.revenue['Classes'] += amount 

    def inadvance(self,number_of_members,amount,begmonth):
        if begmonth == True: 
            self.monthlyAP += number_of_members * amount


    def paycoach(self,number_of_classes): #subtract revenue generated from classes and add as coach expense 
        self.revenue['Classes'] = self.revenue['Classes'] - (number_of_classes * 15)
        self.expenses['Coach'] = self.expenses['Coach'] +  (number_of_classes * 15)

    def payrent(self,amount,endmonth):
        if endmonth == True: 
            self.revenue['Classes'] = self.revenue['Classes'] - amount 
            self.expenses['Rent'] = self.expenses['Rent'] + amount 

    def closemonth(self,endmonth):
        if endmonth == True:
            monthlyprofit = self.revenue['Classes'] - self.expenses['Coach'] - self.expenses['Rent']
        self.log.append(monthlyprofit)

    def resetmonth(self,endmonth):
        if endmonth == True: 
            self.monthlyAP = 0 
            self.revenue['Classes'] = 0 
            self.expenses['Coach'] = 0 
            self.expenses['Rent'] = 0 
        
    def checkdebts(self,endmonth,numcoaches,numclasses,rent):
        potential_coach_debt = numcoaches * numclasses 
        potential_rent_debt = rent 
        if endmonth == True: 
            self.unpaidcoach= potential_coach_debt - self.expenses['Coach'] 
            self.unpaidrent = potential_rent_debt - self.expenses['Rent'] 
        
 
    def UI(self): #creates a window displaying the montly expenses(rent, coach) and monthly revenue
        sg.theme('Dark Blue 3')  # please make your windows colorful
        income_layout = [
        [sg.Text("Revenue")],
        [sg.Listbox(values=[self.revenue['Classes'] ], enable_events=True, size=(25, 1))],]

        expenses_layout = [ 
        [sg.Text("Coach Payments to date")],
        [sg.Listbox(values=[self.expenses['Coach']], enable_events=True, size=(25, 1))],
        [sg.Text("Monthly Rent")],
        [sg.Listbox(values=[self.expenses['Rent']], enable_events=True, size=(25, 1))],]
        layout = [
        [sg.Column(income_layout),
        sg.VSeperator(),
        sg.Column(expenses_layout),]
        ]
        window = sg.Window("Income Statement to date", layout)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
        window.close()


x = IncomeStatement()               
x.UI()
