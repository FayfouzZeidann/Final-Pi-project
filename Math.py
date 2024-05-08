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
        if self.goal == 'Lose weight':
            self._goalweight = self.weight - ((self.weight*20)/100)
        elif self.goal == 'Lose weight slowly':
            self._goalweight = self.weight - ((self.weight*10)/100)
        elif self.goal == 'Maintain weight':
            self._goalweight = self.weight
        elif self.goal == 'Gain weight slowly':
            self._goalweight = self.weight + ((self.weight*10)/100)
        elif self.goal == 'Gain weight':
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
        if self.activity == 'Sedentary':
            return 1.2 * self.get_BMR()
        elif self.activity == 'Moderately active':
            return 1.55 * self.get_BMR()
        elif self.activity == 'Vigorously active':
             return 1.725 * self.get_BMR()
        elif self.activity == 'Extremely active':
            return 1.9 * self.get_BMR()
            
            
    # Function to get recommended calories (based off their choice) and return as a string
    def get_calorie_goal_STR(self):
        if self.goal == 'Lose weight' :
            return f"{round(self.get_TDEE() - 500)}"
        elif self.goal == 'Lose weight slowly':
            return f"{round(self.get_TDEE() - 250)}"
        elif self.goal == 'Maintain weight':
            return f"{round(self.get_TDEE(), 0)}"
        elif self.goal =='Gain weight slowly':
            return f"{round(self.get_TDEE() + 250)}"
        elif self.goal =='Gain weight':
            return f"{round(self.get_TDEE() + 500)}"
        

    #return round(s * 703, 1) &  Function to get recommended calories (based off their choice)
    def get_calorie_goal(self):
        if self.goal == 'Lose weight' :
            return round(self.get_TDEE() - 500, 0)
        elif self.goal == 'Lose weight slowly':
            return round(self.get_TDEE() - 250, 0)
        elif self.goal == 'Maintain weight':
            return round(self.get_TDEE(), 0)
        elif self.goal == 'Gain weight slowly':
            return round(self.get_TDEE() + 250, 0)
        elif self.goal =='Gain weight':
             return round(self.get_TDEE() + 500, 0)
        
    
    # Used to get the macros and it also prints it as a string (this one is only used ofr debugging)
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
        #self.projected_days = []
        if (self.weight == self.goalweight):
            Wc = 0
        else:
            Wc = (self.goalweight - self.weight) / self.days

        for day in range(self.days + 1):
            self.projected_weight.append(round((self.weight + Wc * day), 2)) # might need extra parenthesis
           #self.projected_days.append(day)
        return self.projected_weight
        
    #a similar pbw function, but this takes in a list of stored weights as a refrence
    def create_PBW(self, list): #have to store goal
        projected_weight = []
        goal = self.create_goal(int(list[0]))
        weight = int(list[0])
        #self.projected_days = []
        if (weight == goal):
            Wc = 0
        else:
            Wc = (goal - weight) / self.days

        for day in range(self.days + 1):
            projected_weight.append(round((weight + Wc * day), 2)) # might need extra parenthesis
           #self.projected_days.append(day)
        return projected_weight
    
    #creates goal weight based on goal string
    def create_goal(self, value):
        if self.goal == 'Lose weight' :
            return value - ((value*20)/100)
        elif self.goal == 'Lose weight slowly':
            return value - ((value*10)/100)
        elif self.goal =='Maintain weight':
            return value
        elif self.goal =='Gain weight slowly':
            return value + ((value*10)/100)
        elif self.goal == 'Gain weight':
             return value + ((value*20)/100)
    
    #creates set of plots showing two different sets of data
    def create(self, list, list2):
        plt.scatter([x for x in range(0, len(list))], list, color='blue', marker= 'o')
        plt.plot([x for x in range(0, len(list2))], list2, color='red', linestyle='dotted')
        plt.yticks([])
        plt.title("Your Weight Managment Plan", fontsize=14)
        plt.xlabel("day", fontsize=14)
        plt.ylabel("weight", fontsize =14)
        plt.grid(True)
        #return plt.gcf() #creates figure
        plt.show()

