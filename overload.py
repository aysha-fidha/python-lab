class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length*self.__width
    def __lt__(self,other):
        return self.area()<other.area()
r1=Rectangle(3,4)
r2=Rectangle(5,2)
print("r1<r2:",r1<r2)