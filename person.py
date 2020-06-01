class animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
       return "animal:"+str(self.name)+":"+str(self.age)





class person(animal):
    def __init__(self,name,age):
        animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other):
        diff=self.age-other.age
        print(abs(diff),"year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

print("\n----person tests----")
p1=person("jack",30)
p2=person("jill",25)
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)

