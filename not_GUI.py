import PySimpleGUI as sg
from Math import* #REMOVE THIS EVENTUALLY
from helper_functions import*

#FOR DEBUGGING. REMOVE LATER
days = [x for x in range(0,11)]
weight = [3, 4]
pweight = [x**2 for x in range(0,11)]
DEBUG = False

if DEBUG:
    m = Math("200", "5", "4", "female", "25", 'Moderately active', "Gain weight slowly", '50')
    stored_weights = [200, 200, 200, 202, 203, 204, 200, 203, 204]

#constants
calorie_goal = ''
macros = ''
stored_weights =[]
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
   'Sedentary',
   'Moderately active',
   'Vigorously active',
   'Extremely active'
]

menu_def2 = [
    'Male',
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
        [sg.Text('Feet:', size =(5,1)), sg.InputText(key='-FEET-')],
        [sg.Text('Inches:', size =(5,1)), sg.InputText(key='-INCHES-')],
           [sg.Text('Age:', size =(5,1)), sg.InputText(key='-AGE-')],
           [sg.Text('Gender:', size =(5,1)), sg.Combo(menu_def2, key='-GENDR-')],
           [sg.Text('Activity Level:', size =(5,1)), sg.Combo(menu_def1, key='-ACTLVL-')],
           [sg.Text('Goal:', size =(5,1)), sg.Combo(menu_def3, key='-GOAL-')],
           [sg.Text('Days per Cycle:'), sg.InputText(key='-DAYS-')],
           [sg.Push(), sg.Button('CONTINUE'), sg.Push()]
           ]

layout3 = [[sg.Text('Weight:', size =(5,1)), sg.InputText(key='-WEIGHT-')],
           [sg.Push(), sg.Button('WEIGH!'), sg.Push()]]

layout4 = [
    [sg.Text("Your Daily Calorie Goal is:"), sg.Text(calorie_goal ,key = '-RESULTC-')],
    [sg.Text(macros ,key = '-RESULTM-')],
    [sg.Button('WEIGH AGAIN?'), sg.Push(), sg.Button('CHART')]
    ]

layout5 = [
    [sg.VPush()],
    [sg.Canvas(size= (50, 50), key="-PROJECTED-")], [sg.Canvas(size=(50, 50), key='-ACTUAL-')],
    [sg.VPush()],
    [sg.Push(), sg.Button('BACK'), sg.Push()]

]

# more shenanigans (the main part of the program :/)
layout = [[sg.Column(layout1, key='-COLUMN1-'), sg.Column(layout2, visible=False, key='-COLUMN2-'), sg.Column(layout3, visible=False, key='-COLUMN3-'), sg.Column(layout4, visible=False, key='-COLUMN4-'), sg.Column(layout5, visible=False, key='-COLUMN5-')]]

window = sg.Window('Pi calorie counter', layout).Finalize()


layout = 1  
user_input = []
while True:
    if DEBUG:
        m = Math("200", "5", "4", "female", "25", 'Moderately active', "Gain weight slowly", '50')
        stored_weights = [200, 200, 200, 202, 203, 204, 200, 203, 204]
        m.create_PBW()
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 5
        window[f'-COLUMN{layout}-'].update(visible=True)
        draw_figure(window["-ACTUAL-"].TKCanvas, m.create(stored_weights))

    pbw = []
    '''
    if DEBUG:
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 5
        window[f'-COLUMN{layout}-'].update(visible=True)
        draw_figure(window["-PROJECTED-"].TKCanvas, m.create(stored_weights))
        '''
    event, values = window.read()
    print(event, values)
    #user_input.append(values.values())
    #print(user_input) #where do i put this--its FINE they dont even work
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
        m = Math(values['-WEIGHT-'], values['-FEET-'], values['-INCHES-'], values['-GENDR-'], values['-AGE-'], values['-ACTLVL-'], values['-GOAL-'], values['-DAYS-'])
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 4
        window[f'-COLUMN{layout}-'].update(visible=True)
        calorie_goal = m.get_calorie_goal_STR()
        macros = m.get_macros()
        stored_weights.append(values['-WEIGHT-'])
        window['-RESULTC-'].update(calorie_goal)
        window['-RESULTM-'].update(macros)
    # Addition by Eli, I think we should have some sort of way to weigh yourself again
    # possibly store the previous weight in a var? and move on to the next?
    if event == 'WEIGH AGAIN?':
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 3
        window[f'-COLUMN{layout}-'].update(visible=True)
    if event == 'CHART':
        #figure = generate_figure_plot([x for x in range(0,11)])
        pbw = m.create_PBW(stored_weights)
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 5
        window[f'-COLUMN{layout}-'].update(visible=True)
        if int(stored_weights[0]) == m.goalweight:
            draw_figure(window["-ACTUAL-"].TKCanvas, m.create(stored_weights,pbw))
        if int(stored_weights[0]) > m.goalweight:
            draw_figure(window["-ACTUAL-"].TKCanvas, m.create(stored_weights,[(m.create_goal(int(stored_weights[0]))-int(stored_weights[0])/int(m.days))+int(stored_weights[0])*-x for x in range(int(m.days) +1)]))
        if int(stored_weights[0]) < m.goalweight:
            draw_figure(window["-ACTUAL-"].TKCanvas, m.create(stored_weights,[(m.create_goal(int(stored_weights[0]))-int(stored_weights[0])/int(m.days))+int(stored_weights[0])*x for x in range(int(m.days) +1)]))
        print(pbw)
        print(stored_weights)
    if event == 'BACK':
        window[f'-COLUMN{layout}-'].update(visible=False)
        layout = 4
        window[f'-COLUMN{layout}-'].update(visible=True)
        

window.close()





