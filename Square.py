#Lab 02 - Nealson Setiawan
#Square Class

from Shape2D import Shape2D

class Square(Shape2D):

    def __init__(self,color,side):
        self.shape = "SQUARE"
        self.color = color
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        return self.side ** 2

    def computePerimeter(self):
        return 4 * self.side

    def getShapeProperties(self):
        string = "Shape: {}, Color: {}, Side: {}, Area: {}, Perimeter: {}"\
            .format(self.shape, self.color, self.getSide(), self.computeArea(), self.computePerimeter())
        return string

    