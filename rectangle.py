class Rectangle:
    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
r1=Rectangle(4,5)
r2=Rectangle(3,5)
if r1.area()>r2.area():
    print("r1 has the larger area")
elif r1.area()<r2.area():
    print("r2 has the smaller area")
else:
    print("Both rectangles have equal area")