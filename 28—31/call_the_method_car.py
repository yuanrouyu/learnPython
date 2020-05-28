class Car(object):
    def __init__(self,w,d):
        self.wheels=w
        self.doors=d
        self.color=""
    def paint(self,c):
        self.color=c
mycar=Car(4,2)
mycar.paint("red")
print(mycar.wheels)
print(mycar.doors)
print(mycar.color)