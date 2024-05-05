import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
'''
def generate_figure_scatter(list):
    plt.scatter([x for x in range(len(list))], list, color='blue', marker= 'o')
    #plt.plot([x for x in range(len(pbw))], pbw, color='red', marker = 'o')
    plt.yticks([])
    plt.title("Your Weight Managment Plan", fontsize=14)
    plt.xlabel("day", fontsize=14)
    plt.ylabel("weight", fontsize =14)
    plt.grid(True)
    return plt.gcf() #creates figure

def generate_figure_plot(list):
    #plt.scatter([x for x in range(len(list))], list, color='blue', marker= 'o')
    plt.plot([x for x in range(len(list))], list, color='red', marker = 'o')
    plt.yticks([])
    plt.title("Your Weight Managment Plan", fontsize=14)
    plt.xlabel("day", fontsize=14)
    plt.ylabel("weight", fontsize =14)
    plt.grid(True)
    return plt.gcf() #creates figure
    '''

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
