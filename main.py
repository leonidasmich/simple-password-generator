import PySimpleGUI as sg 
import random  

sg.theme('Black')
layout = [
    [sg.Text('Please Generate your Password')],
    [sg.Button('Generate', key = '-GENERATE-'), sg.Text('Password:', key = '-OUTPUT-')]
]

window = sg.Window('Password Generator', layout, icon = './favicon.ico')

name = ''
numbers = ['1','2','3','4','5','6','7','8','9','0']
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charactersup = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*']

        
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-GENERATE-':
        password = random.sample(numbers, 5) + random.sample(characters, 7) + random.sample(symbols, 4) + random.sample(charactersup, 2)
        x = " ,".join(password)
        y = x.replace(',', '')
        save = y.replace(' ', '')
        window['-OUTPUT-'].update(save)
                  
window.close()