import PySimpleGUI as sg

rent = 500 

revenue = {'Classes': 0}
listofmonths = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
log = [0]*12


sg.theme('Dark Blue 3')  # please make your windows colorful
profit_layout = [
        [sg.Text("Profits for the year")],
        [sg.Listbox(values=[log], enable_events=True, size=(25, 1))],
        [sg.Listbox(values=[listofmonths], enable_events=True, size=(25, 1))],]

profitwindow = sg.Window("Yearly profits", profit_layout)
event, values =  profitwindow.read()
