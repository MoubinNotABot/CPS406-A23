import PySimpleGUI as sg

rent = 200 
months = {0: 'Jan', 1:'Feb', 2:'Mar',3:'Apr', 4:'May',5:'June',6:'July',7:'August',8:'September',9:'October',10:'November',11:'December'}

sg.theme('Dark Blue 3')  # please make your windows colorful

class IncomeStatement: 
    def __init__(self):
        self.revenue = {'Classes': 0}
        self.expenses = {'Coach': 0, 'Rent':200}
        self.log = [0]*12
        self.monthlyAP = 0
        self.rentdebt = [0]*12
        self.unpaidcoach = [0]*12
        self.currentmonth = 0 
    
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
             self.log = [0]*12
             self.monthlyAP = 0
             self.rentdebt = [0]*12
             self.unpaidcoach = [0]*12 
             self.currentmonth = 0 
    
    # def runclass(self,number_of_attendees,class_price,classended):
    #     if classended == True: 
    #         self.revenue['Class'] += number_of_attendees * class_price
    
    def addtorevenue(self, amount): #anytime someone makes a payment, add to revenue generated from classes 
        self.revenue['Classes'] += amount 

    def inadvance(self,number_of_members,amount,begmonth):
        if begmonth == True: 
            self.monthlyAP += number_of_members * amount


    def updatecoachexpense(self,number_of_classes): #subtract revenue generated from classes and add as coach expense 
        self.expenses['Coach'] = self.expenses['Coach'] +  (number_of_classes * 15)
        return None 

    def paycoach(self): #subtract revenue generated from classes and add as coach expense 
        coachpayment_layout = [[sg.Text(f'Enter amount to pay coach')],
          [sg.Input()],
          [sg.Button('Enter'),sg.Exit()]]
        caochpaymentwindow = sg.Window("Pay rent", coachpayment_layout)
        while True:
            event, values = caochpaymentwindow.read()
            if (event == "Exit") or (event == sg.WIN_CLOSED):
                caochpaymentwindow.close()
                break
            elif (event == 'Enter'):
                amount = values[0] 
                self.expenses['Coach'] = self.expenses['Coach'] -  int(amount)
                caochpaymentwindow.close()
        return None 


    def payrent(self):
        renttobepaid = self.expenses['Rent']
        rentpayment_layout = [
         [sg.Text(f'Rent remaining to be paid for the month of {months[self.currentmonth]} is {renttobepaid}, enter amount to pay')],
         [sg.Input()],
        [sg.Button('Enter'),sg.Exit()]]
        rentpaymentwindow = sg.Window("Pay rent", rentpayment_layout)
        while True:
            event, values = rentpaymentwindow.read()
            if (event == "Exit") or (event == sg.WIN_CLOSED):
                rentpaymentwindow.close()
                break
            elif (event == 'Enter'):
                amount = values[0] 
                self.expenses['Rent'] = self.expenses['Rent'] -  int(amount)
                print (self.expenses['Rent'])
                rentpaymentwindow.close()
        return None 
        
    def closemonth(self,endmonth):
        if endmonth == True:
            monthlyprofit = self.revenue['Classes'] - self.expenses['Coach'] - self.expenses['Rent']
            self.log[self.currentmonth] = monthlyprofit 
            if self.expenses['Rent'] > 0:
                self.rentdebt[self.currentmonth] = self.expenses['Rent'] 
            if self.expenses['Coach'] > 0:
                self.unpaidcoach[self.currentmonth] = self.expenses['Coach'] 
            self.currentmonth += 1 
            self.resetmonth(True)
        return None 

    def resetmonth(self,endmonth):
        if endmonth == True: 
            self.monthlyAP = 0 
            self.revenue['Classes'] = 0 
            self.expenses['Coach'] = 0 
            self.expenses['Rent'] = rent 
        
    # def checkdebts(self,endmonth,numcoaches,numclasses,rent):
    #     potential_coach_debt = numcoaches * numclasses 
    #     potential_rent_debt = rent 
    #     if endmonth == True: 
    #         self.unpaidcoach= potential_coach_debt - self.expenses['Coach'] 
    #         self.unpaidrent = potential_rent_debt - self.expenses['Rent'] 
        
 
    def UI(self): #creates a window displaying the montly expenses(rent, coach) and monthly revenue
        sg.theme('Dark Blue 3')  # please make your windows colorful
        income_layout = [
        [sg.Text("Revenue")],
        [sg.Listbox(values=[self.revenue['Classes'] ], enable_events=True, size=(25, 1))],]

        expenses_layout = [ 
        [sg.Text("Coach Payments")],
        [sg.Listbox(values=[self.expenses['Coach']], enable_events=True, size=(25, 1))],
        [sg.Text("Monthly Rent")],
        [sg.Listbox(values=[self.expenses['Rent']], enable_events=True, size=(25, 1))],]
        layout = [
        [sg.Column(income_layout),
        sg.VSeperator(),
        sg.Column(expenses_layout),]
        ]
        window = sg.Window(f'Income Statement for the month of {months[self.currentmonth]}', layout)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
        window.close()
        return None 

    def seeprofits(self):
        sg.theme('Dark Blue 3')  # please make your windows colorful
        profit_layout = [
        [sg.Text("Profits for the year")],
        [sg.Listbox(values=[self.log], enable_events=True, size=(20, 12))],]
        profitwindow = sg.Window("Yearly profits", profit_layout)
        event, values =  profitwindow.read()
        while event != sg.WIN_CLOSED:
            event, values = profitwindow.read()
        if event == sg.WIN_CLOSED:
            profitwindow.close()
        return None 

    def seedebts(self):
        sg.theme('Dark Blue 3')  # please make your windows colorful
        profit_layout = [
        [sg.Text("Rent debts for the year")],
        [sg.Listbox(values=[self.rentdebt], enable_events=True, size=(20, 12))],
        [sg.Text("Unpaid coach expenses for the year")],
        [sg.Listbox(values=[self.unpaidcoach], enable_events=True, size=(20, 12))],
        ]
        debtwindow = sg.Window("Yearly profits", profit_layout)
        event, values =  debtwindow.read()
        while event != sg.WIN_CLOSED:
            event, values = debtwindow.read()
        if event == sg.WIN_CLOSED:
            debtwindow.close()
        return None 





