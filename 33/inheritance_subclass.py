class animals(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,nweage):
        self.age=nweage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class cat(animal):
    def speak(self):
        print("miao")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)