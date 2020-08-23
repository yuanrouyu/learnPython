


# yuan=input()
# print(yuan)

# class Coordinate(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def distance(self,other):
#         x_diff_sq=(self.x-other.x)**2
#         y_diff_sq=(self.y-other.y)**2
#         return (x_diff_sq+y_diff_sq)**0.5
#     def __str__(self):
#         return "<"+str(self.x)+","+str(self.y)+">"
# c=Coordinate(3,4)
# print(c)
# print(type(c))
# print(Coordinate)
# print(type(Coordinate))
# print(isinstance(c,Coordinate))

# class Car(object):
#     def __init__(self,w,d,x):
#         self.wheels=w
#         self.doors=d
#         self.color=""
#         self.shape=""

#     def paint(self,c,h):
#         self.color=c
#         self.shape=h
   
# mycar=Car(4,2)
# mycar.paint("red","round")
# print(mycar.wheels)
# print(mycar.doors)
# print(mycar.color)
# print(mycar.shape)


# def set_name(self,newname=""):
#     self.name=newname

# a=animal(3)
# a.set_name()
# print(a.get_name())

# a=animal(3)
# a.set_name("fluffy")
# print(a.get_name())


try:
    r=10/a
    print(r)
except:
    raise ValueError()