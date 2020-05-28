class Car(object):
    def __init__(self,w,d):
        self.wheels=w
        self.doors=d
        self.color=""
        self.shape=""
    def paint(self,c,h):
        self.color=c
        self.shape=h
mycar=Car(4,2)
mycar.paint("red","round")
print(mycar.wheels)
print(mycar.doors)
print(mycar.color)
print(mycar.shape)
