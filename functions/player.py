class player:

    def __init__(self,name, point=60, value=""):
        self.name = name
        self.points = point
        self.value = value

    def get_points(self):
        return self.points
      
    def set_points(self, x=0):
        self.points = x

    def get_name(self):
        return self.name
      
    def set_name(self, x=""):
        self.name = x
    
    def get_value(self):
        return self.value
      
    def set_value(self, x=0):
        self.value = x

    def smart_add_points(add_points):
        def inner(value):
            print("It add points")
            if value <= 0:
                print("The value points is not true format!!!")
                return
            return add_points(value)
        return inner

    @smart_add_points
    def add_points(self, value):
        self.points += value