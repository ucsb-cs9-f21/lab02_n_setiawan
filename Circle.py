#Lab 02 - Nealson Setiawan
#Circle Class

from Shape2D import Shape2D

class Circle(Shape2D):
    def __init__(self,color,radius):
        self.color = color
        self.shape = "CIRCLE"
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius
    
    def computeArea(self):
        a = self.radius ** 2 * 3.14159
        return a

    def computePerimeter(self):
        b = self.radius * 3.14159 * 2
        return b

    def getShapeProperties(self):
        string = "Shape: {}, Color: {}, Radius: {}, Area: {}, Perimeter: {}".format(self.shape, self.color, self.radius, self.computeArea(), self.computePerimeter())
        return string

    