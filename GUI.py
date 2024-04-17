import PySimpleGUI as sg
from Math import* #REMOVE THIS EVENTUALLY

calorie_goal = ''
macros = ''
my_theme = {'BACKGROUND': '#ffffff',
                'TEXT': '#000000',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('#35680f', '#7be62b'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('Wiifit', my_theme)


sg.theme('Wiifit')


# shenanigans
menu_def1 = [
   ['Sedentary'],
   'Moderately active',
   'Vigorously active',
   'Extremely active'
]

menu_def2 = [
    ['Male'],
    'Female',
    
]

menu_def3 = [
    'Lose weight',
    'Lose weight slowly',
    'Maintain weight', 
    'Gain weight slowly', 
    'Gain weight'
]
layout1 = [[sg.Image("not_wii_fit.png")],
           [sg.Push(), sg.Button('START'), sg.Push()]
           ]

layout2 = [[sg.Text('Before we begin, please provide the following information:', justification= "center")],
        [sg.Text('Feet:', size =(5,1)), sg.InputText(key='-FEET-'), sg.Push(), sg.Text('Inches:', size =(5,1)), sg.InputText(key='-INCHES-')],
           [sg.Text('Age:', size =(5,1)), sg.InputText(key='-AGE-')],
           [sg.Text('Gender:', size =(5,1)), sg.Combo(menu_def2, key='-GENDR-')],
           [sg.Text('Activity Level:', size =(5,1)), sg.Combo(menu_def1, key='-ACTLVL-')],
           [sg.Text('Goal:', size =(5,1)), sg.Combo(menu_def3, key='-GOAL-')],
           [sg.Push(), sg.Button('CONTINUE'), sg.Push()]
           ]

layout3 = [[sg.Text('Weight:', size =(5,1)), sg.InputText(key='-WEIGHT-')],
           [sg.Push(), sg.Button('WEIGH!'), sg.Push()]]

layout4 = [
    [sg.Text("Your Daily Calorie Goal is:"), sg.Text(calorie_goal ,key = '-RESULTC-')],
    [sg.Text(macros ,key = '-RESULTM-')]]

# more shenanigans (the main part of the program :/)
layout = [[sg.Column(layout1, key='-COLUMN1-'), sg.Column(layout2, visible=False, key='-COLUMN2-'), sg.Column(layout3, visible=False, key='-COLUMN3-'), sg.Column(layout4, visible=False, key='-COLUMN4-')]]
    


window = sg.Window('Pi calorie counter', layout)

layout = 1  
user_input = []
while True:
    event, values = window.read()
    print(event, values)
    #user_input.append(values.values())
   # print(user_input) #where do i put this--its FINE they dont even work
    if event in (None, 'Exit'):
        break
    if event == 'START':
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 2
        window[f'-COLUMN{layout}-'].update(visible=True)
    if event == 'CONTINUE':
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 3
        window[f'-COLUMN{layout}-'].update(visible=True)
    if event == 'WEIGH!':
        m = Math(values['-WEIGHT-'], values['-FEET-'], values['-INCHES-'], values['-GENDR-'], values['-AGE-'], values['-ACTLVL-'], values['-GOAL-'])
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 4
        window[f'-COLUMN{layout}-'].update(visible=True)
        #string = str(Whatever(values['-HEIGHT-'])) #IT WORKS RAHH. this is the wrong class though
        calorie_goal = m.get_calorie_goal_STR()
        macros = m.get_macros()
        window['-RESULTC-'].update(calorie_goal)
        window['-RESULTM-'].update(macros)
window.close()





