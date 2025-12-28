import  math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius
    

#Taking input
r=float(input("Enter radius of the circle:"))

#Creating object
c=Circle(r)

#Displaying result
print("Area of circle =",c.area())
print("perimeter of circle =",c.perimeter())
