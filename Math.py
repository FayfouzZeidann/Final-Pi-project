#some constats to test things out 
WEIGHT = 145
HEIGHT = 64
GENDER = True

ACTIVITY_LEVELS = ['Sedentary',
   'Moderately active',
   'Vigorously active',
   'Extremely active']


class Math:
    def __init__(self, weight, height, gender, age, activity, goal) -> None:
        self.weight = weight
        self.height = height 
        self.gender = gender
        self.age = age
        self.activity = activity
        self.goal = goal

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            self._weight = 1

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            self._height = 1

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, string):
        if string == 'female':
            self._gender = True
        elif string == 'male':
            self.gender = False

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            self._age = 1
    
    @property
    def activity(self):
        return self._activity
    
    @activity.setter
    def activity(self, string):
        self._activity = string
        
    def get_BMI(self):
        s = (self.weight/(self.height)**2)
        return round(s * 703, 1)
    
    def get_BMR(self):
        if self.gender == False: #male
            return 66 + (6.23* self.weight) + (12.7 *self.height) - (6.8 * self.age)
        elif self.gender == True: #female
            return 655 + (4.35 *self.weight) + (4.7 *self.height) -(4.7* self.age)
        
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
            
    def get_calorie_goal(self):
         match self.goal:
            case 'Lose weight':
                return self.get_TDEE() - 500
            case 'Lose weight slowly':
                return self.get_TDEE() - 250
            case 'Maintain weight':
                return self.get_TDEE()
            case 'Gain weight slowly':
                return self.get_TDEE() + 250
            case 'Gain weight':
                return self.get_TDEE() + 500
            
            
            
            
                
            