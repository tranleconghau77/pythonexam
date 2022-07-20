class player:

    def __init__(self,name, point=60, value=""):
        self.name = name
        self.points = point
        self.value = value

    def add_point(self, value):
        self.points += value

    def get_points(self):
        return self.points
      
    def set_points(self, x):
        self.points = x

    def get_name(self):
        return self.name
      
    def set_name(self, x):
        self.name = x
    
    def get_value(self):
        return self.value
      
    def set_value(self, x):
        self.value = x