#Lab 02 - Nealson Setiawan
#Shape2D Class

class Shape2D:

    def __init__(self, color):
        self.color = color
        self.shape = "N/A"

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def getShapeProperties(self):
        string = "Shape: {}, Color: {}".format(self.shape, self.color)
        return string
