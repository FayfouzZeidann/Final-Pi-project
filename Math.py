#some constats to test things out 
WEIGHT = 145
HEIGHT = 64
GENDER = True





class Math:
    def __init__(self, weight, height, gender, age, activity) -> None:
        self.weight = weight
        self.height =  height 
        self.gender = gender
        self.age = age
        self.activity = activity

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
            