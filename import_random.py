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



class student(person):
    def __init__(self,name,age,major=None):
        person.__init__(self,name,age)
        self.major=major
    def change_major(self,major):
        self.major=major
    def speak(self):
        r=random.random()
        if r<0.25:
            print("i have homework")
        elif 0.25<=r<0.5:
            print("i need sleep")
        elif 0.5<=r<0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.name)+":"+str(self.major)
