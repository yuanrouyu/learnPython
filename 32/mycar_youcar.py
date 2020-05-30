class Car(object):
    def __init__(self,w,d):
        self.wheels=w
        self.doors=d
        self.color=""
        self.shape=""
    def paint(self,c):
        self.color=c
    def __eq__(self,other):
        if self.wheels==other.wheels and\
           self.color==other.color and\
           self.doors==other.doors:
           return True
        else:
           return False

mycar=Car(4,2)
mycar.paint("red")
youcar=Car(4,2)
print(mycar==youcar)


