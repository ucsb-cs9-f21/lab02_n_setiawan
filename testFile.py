from Shape2D import Shape2D
from Circle import Circle
from Square import Square

s1 = Shape2D("blue")
assert s1.getShapeProperties() == "Shape: N/A, Color: blue"

c1 = Circle("blue", 2.5)
assert c1.computeArea() == 19.6349375
assert c1.computePerimeter() == 15.70795
assert c1.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 2.5, Area: 19.6349375, Perimeter: 15.70795"

sq1 = Square("blue", 2.5)
assert sq1.getShapeProperties() == "Shape: SQUARE, Color: blue, Side: 2.5, Area: 6.25, Perimeter: 10.0"