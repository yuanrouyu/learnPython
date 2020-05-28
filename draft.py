class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
c=Coordinate(3,4)
print(c)
print(type(c))
print(Coordinate)
print(type(Coordinate))
print(isinstance(c,Coordinate))
