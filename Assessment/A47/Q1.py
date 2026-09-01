class Shape:
     def calculatearea(self):
          print("Area calculation not defined for Shape")

class circle:
     def __init__(self,r):
            self.r=r
     def calculatearea(self):
          self.area=3.14 *self.r*self.r
          print("area is ciccle is = ",self.area)

class rectangle:
     def __init__(self,l,b):
          self.l=l
          self.b=b
     def calculatearea(self):
          self.area=self.l*self.b
          print("area of rectangle = ",self.area)

shapes = [
    Shape(),
    circle(5),
    rectangle(4, 6)
]

for shape in shapes:
    shape.calculatearea()