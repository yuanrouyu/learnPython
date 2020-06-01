## 33课
### inheritance


```python
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
```
```
    object:
    -everything is an object
    -class object
    implements basic
    operations in pythin,like binding variables,etc
```
```python
class cat(animal):
    def speak(self):
        print("miao")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
```

```
    inheritance subclass
    animal:inherits all atributes of animal:
    __init__()
    age,name
    get_age(),get_name()
    set_age(),set_name()
    __str__()
    def speak(self):  add new functionality via speak method
    def __str__(self): overrides__str__  (重写)
 ```
 ```python
    class person(animals):
    def __init__(self,name,age):
        animals.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_giff(self,other):
        diff=self.age-other.age
        print(abs(diff),"year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
 ```
 ```
    animal:paren class is animal
    animal.__init__(self,age):call animal constructor
    self.set_name(name):call animals method
    self.friends=[]:add a new data attribute


    def get_friends(self):
    def add_friends(self,fname):
    def speak(self):
    def age_giff(self,other):
    new method



 ```
