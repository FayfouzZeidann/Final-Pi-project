#some constats to test things out 
WEIGHT = 145
HEIGHT = 64
GENDER = True

ACTIVITY_LEVELS = ['Sedentary',
   'Moderately active',
   'Vigorously active',
   'Extremely active']

class Math:
    def __init__(self, weight, feet, inches, gender, age, activity, goal, days = 1) -> None:
        self.weight = weight
        self.height = self.find_height(feet, inches) 
        self._gender = gender
        self.age = age
        self.activity = activity
        self.goal = goal
        self.days = days

    # Getter and Setter for weight
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
     
    # function to get and store their daily body weight
    def get_daily_weight(self):
        pass

    # gets todays date
    def get_day(self): # dunno if we need this 
        pass

    # method to create projected body weight
    def create_PBW(self):
        PBW = {}
        if (self.weight == self.goal):
            Wc = 0
        else:
            Wc = (self.goal - self.weight) / self.days

        for day in range(self.days + 1):
            PBW[day] = round((self.weight + Wc * day), 2) # might need extra parenthesis
        return PBW

    # function to track daily weight
    # needs some fixing
    def create_ABW(self):
        ABW = {}
        # ABW[get_day()] = round((get_daily_weight()))
        return ABW

            
