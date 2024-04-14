import PySimpleGUI as sg

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
        [sg.Text('Height:', size =(5,1)), sg.InputText(key='-HEIGHT-')],
           [sg.Text('Age:', size =(5,1)), sg.InputText(key='-AGE-')],
           [sg.Text('Gender:', size =(5,1)), sg.Combo(menu_def2, key='-GENDR-')],
           [sg.Text('Activity Level:', size =(5,1)), sg.Combo(menu_def1, key='-ACTLVL-')],
           [sg.Text('Goal:', size =(5,1)), sg.Combo(menu_def3, key='-GOAL-')],
           [sg.Push(), sg.Button('CONTINUE'), sg.Push()]
           ]

layout3 = [[sg.Text('Weight:', size =(5,1)), sg.InputText(key='-WEIGHT-')]]

# more shenanigans (the main part of the program :/)
layout = [[sg.Column(layout1, key='-COLUMN1-'), sg.Column(layout2, visible=False, key='-COLUMN2-'), sg.Column(layout3, visible=False, key='-COLUMN3-')]]
    


window = sg.Window('(as of now unamed) Fitness Application', layout)

layout = 1  
user_input = {}
while True:
    event, values = window.read()
    print(event, values)
    print(user_input)
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
window.close()




