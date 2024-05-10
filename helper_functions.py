import numpy
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#creates goal outside the Math class. creating it within the same option was causing issues
def create_goal(weight, goal):
        if goal == 'Lose weight':
            return weight - ((weight*20)/100)
        if goal == 'Lose weight slowly':
            return weight - ((weight*10)/100)
        if goal == 'Maintain weight':
            return weight
        if goal == 'Gain weight slowly':
            return weight + ((weight*10)/100)
        if goal == 'Gain weight':
            return weight + ((weight*20)/100)

#draws a figure onto a canvas
def draw_figure(canvas, figure):
    agg =FigureCanvasTkAgg(figure, canvas)
    agg.draw()
    agg.get_tk_widget().pack()
    return agg
