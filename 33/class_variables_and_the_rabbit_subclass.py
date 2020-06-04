class animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,newname):
        self.name=newname
    def set_age(self,newage):
        self.age=newage
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
        
class rabbit(animal):
    tag=1
    def __init__(self,age,parent1=None,parent2=None):
        animal.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=rabbit.tag
        rabbit.tag +=1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self,other):
        return rabbit(0,self,other)
    def __eq__(self,other):
        parents_same=self.parent1.rid==other.parent1.rid\
            and self.parent2.rid==other.parent2.rid
        parents_opposite=self.parent2.rid==other.parent1.rid\
            and self.parent1.rid==other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+str(self.rid).zfill(3)


print("\n----tests rabbit----")
r1=rabbit(3)
r2=rabbit(4)
r3=rabbit(5)
print("r1:",r1)
print("r2:",r2)
print("r3:",r3)
print("r1 parent1:",r1.get_parent1())
print("r1 paretn2:",r1.get_parent2())

print("\n----add----")
r4=r1+r2
print("r1:",r1)
print("r2:",r2)
print("r4:",r4)
print("r4 parent1:",r4.get_parent1())
print("r4 parent2:",r4.get_parent2())

print("\n----eq----")
r5=r3+r4
r6=r4+r3
print("r3:",r3)
print("r4:",r4)
print("r5:",r5)
print("r6:",r6)
print("r5 parent1:",r5.get_parent1())
print("r5 parent2:",r5.get_parent2())
print("r6 parent1:",r6.get_parent1())
print("r6 parent2:",r6.get_parent2())
print("r5 amd r6 have same parents?",r5==r6)
print("r4 amd r6 have same parents?",r4==r6)







