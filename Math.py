import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Math:
    def __init__(self, weight, feet, inches, gender, age, activity, goal, days = 1) -> None:
        self.weight = weight
        self.height = self.find_height(feet, inches) 
        self._gender = gender
        self.age = age
        self.activity = activity
        self.goal = goal
        self.goalweight = 0
        self.days = days
        

    # Getter and Setter for weight
    @property
    def goalweight(self):
        return self._goalweight
    
    @goalweight.setter
    def goalweight(self, value):
        match self.goal:
            case 'Lose weight':
                self._goalweight = self.weight - ((self.weight*20)/100)
            case 'Lose weight slowly':
                self._goalweight = self.weight - ((self.weight*10)/100)
            case 'Maintain weight':
                self._goalweight = self.weight
            case 'Gain weight slowly':
                self._goalweight = self.weight + ((self.weight*10)/100)
            case 'Gain weight':
                self._goalweight = self.weight + ((self.weight*20)/100)


    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        value = int(value)
        if value > 0:
            self._weight = value
        else:
            self._weight = 1

    # Getter and Setter for Height
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        value = int(value)
        if value > 0:
            self._height = value
        else:
            self._height = 1
    
    # Getter and Setter for Gender
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, string):
        if string == 'Female':
            self._gender = True
        elif string == 'Male':
            self._gender = False

    # Getter and Setter for Age
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        value = int(value)
        if value > 0:
            self._age = value
        else:
            self._age = 1
    
    # Getter and Setter for Activity
    @property
    def activity(self):
        return self._activity
    
    @activity.setter
    def activity(self, string):
        self._activity = string

    # Getter and setter for days
    @ property
    def days(self):
        return self._days
    
    @ days.setter
    def days(self, value):
        value = int(value)
        if value <= 0:
            self._days = 1
        else: 
            self._days = value

    # Getter and setter for the current day
    @ property
    def currentDay(self):
        return self._currentDay
    
    @ currentDay.setter
    def currentDay(self, value):
        self._currentDay = self._currentDay + value

    # Function to find height
    def find_height(self, ft, inch):
        ft = int(ft)
        inch = int(inch)
        return (ft/12) + inch

    # Function get the person's BMI
    def get_BMI(self):
        s = (self.weight/(self.height)**2)
        return round(s * 703, 1)
    
    # Function used to get a person's BMR (depending on gender)
    def get_BMR(self):
        if self.gender == False: #male
            return 66 + (6.23* self.weight) + (12.7 *self.height) - (6.8 * self.age)
        else:
            return 655 + (4.35 *self.weight) + (4.7 *self.height) -(4.7* self.age)
        
    # Function to get a person's TDEE (depending on their option)
    def get_TDEE(self):
        match self.activity:
            case 'Sedentary':
                return 1.2 * self.get_BMR()
            case 'Moderately active':
                return 1.55 * self.get_BMR()
            case 'Vigorously active':
                return 1.725 * self.get_BMR()
            case 'Extremely active':
                return 1.9 * self.get_BMR()
            
    # Function to get recommended calories (based off their choice) and return as a string
    def get_calorie_goal_STR(self):
         match self.goal:
            case 'Lose weight':
                return f"{round(self.get_TDEE() - 500)}"
            case 'Lose weight slowly':
                return f"{round(self.get_TDEE() - 250)}"
            case 'Maintain weight':
                return f"{round(self.get_TDEE(), 0)}"
            case 'Gain weight slowly':
                return f"{round(self.get_TDEE() + 250)}"
            case 'Gain weight':
                return f"{round(self.get_TDEE() + 500)}"

    #return round(s * 703, 1) &  Function to get recommended calories (based off their choice)
    def get_calorie_goal(self):
        match self.goal:
            case 'Lose weight':
                return round(self.get_TDEE() - 500, 0)
            case 'Lose weight slowly':
                return round(self.get_TDEE() - 250, 0)
            case 'Maintain weight':
                return round(self.get_TDEE(), 0)
            case 'Gain weight slowly':
                return round(self.get_TDEE() + 250, 0)
            case 'Gain weight':
                return round(self.get_TDEE() + 500, 0)
    
    # Used to get the macros and it also prints it as a string
    def get_macros(self): # Calculates macros for what you want to do
        return f"Balanced:\
        \nCarbs-{round((self.get_calorie_goal()*0.4)/4)}g\
        Fat-{round((self.get_calorie_goal()*0.3)/9)}g\
        Protien-{round((self.get_calorie_goal()*0.3)/4)}g\
        \n\nWeight Loss:\
        \nCarbs-{round((self.get_calorie_goal()*0.25)/4)}g\
        Fat-{round((self.get_calorie_goal()*0.25)/9)}g\
        Protien-{round((self.get_calorie_goal()*0.50)/4)}g\
        \n\nBody Builing:\
        \nCarbs-{round((self.get_calorie_goal()*0.60)/4)}g\
        Fat-{round((self.get_calorie_goal()*0.15)/9)}g\
        Protien-{round((self.get_calorie_goal()*0.25)/4)}g" 
   

    # method to create projected body weight
    def create_PBW(self):
        self.projected_weight = []
        self.projected_days = []
        if (self.weight == self.goalweight):
            Wc = 0
        else:
            Wc = (self.goalweight - self.weight) / self.days

        for day in range(self.days + 1):
            self.projected_weight.append(round((self.weight + Wc * day), 2)) # might need extra parenthesis
            self.projected_days.append(day)
        

    
    def create_plot(self, weight):
        self.create_PBW()
        x = self.projected_days
        y = self.projected_weight
        x2 = []
        for day in range(len(weight)):
            x2.append(day)
        fig, ax = plt.subplots(1,1)
        ax.plot(x,y,label='Projected body weight')
        ax.plot(x2,weight,label='Daily body weight')
        ax.set_xlabel('Day Number')
        ax.set_ylabel('Projected Weight')
        ax.set_title('Projected BW vs Daily BW')
        x_axis = 0
        x_axis_list = []
        while x_axis < (self.days + 10):
            x_axis_list.append(x_axis)
            x_axis += 10
        ax.set_xticks(x_axis_list)
        ax.plot(x,y, color='green')
        ax.legend()
        plt.show() #MAKE SURE TO CORRECTLY SIZE THE PLOT

            
