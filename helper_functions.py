import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_figure(day, pbw, abw):
    plt.scatter(day, abw, color='blue', marker= 'o')
    plt.plot(day, pbw, color='red', marker = 'o')
    plt.yticks([])
    plt.title("Your Weight Managment Plan", fontsize=14)
    plt.xlabel("day", fontsize=14)
    plt.ylabel("weight", fontsize =14)
    plt.grid(True)
    return plt.gcf() #creates figure

def draw_figure(canvas, figure):
    agg =FigureCanvasTkAgg(figure, canvas)
    agg.draw()
    agg.get_tk_widget().pack(side='top', fill="both", expand=1)
    return agg
