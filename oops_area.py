class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  
        return 3.14159 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  
        return self.side * self.side

shapes =Circle(5)
print("Area of circle is :",shapes.area())  