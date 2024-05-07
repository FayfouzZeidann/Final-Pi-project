import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np 

def frequent(list):
     unique, count = np.unique(list, return_counts=True)
     i = np.argmax(count)
     return unique[i]
    
def create_PBW(list, goal, days): #have to store goal
    projected_weight = []
    weight = int(list[0])
    #self.projected_days = []
    if (weight == goal):
        Wc = 0
    else:
        Wc = (goal - weight) / days

    for day in range(days + 1):
        projected_weight.append(round((weight + Wc * day), 2)) # might need extra parenthesis
        #self.projected_days.append(day)
    return projected_weight

def create(list, list2):
        plt.scatter([x for x in range(0, len(list))], list, color='blue', marker= 'o')
        plt.plot([x for x in range(0, len(list2))], list2, color='red', linestyle='dotted')
        plt.yticks([])
        plt.title("Your Actual Weight", fontsize=14)
        plt.xlabel("day", fontsize=14)
        plt.ylabel("weight", fontsize =14)
        plt.grid(True)
        return plt.gcf() #creates figure

def create_goal(weight, goal):
        match goal:
            case 'Lose weight':
                return weight - ((weight*20)/100)
            case 'Lose weight slowly':
                return weight - ((weight*10)/100)
            case 'Maintain weight':
                return weight
            case 'Gain weight slowly':
                return weight + ((weight*10)/100)
            case 'Gain weight':
                return weight + ((weight*20)/100)

def draw_figure(canvas, figure):
    agg =FigureCanvasTkAgg(figure, canvas)
    agg.draw()
    agg.get_tk_widget().pack(side='top', expand=1)
    return agg
