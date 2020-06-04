## 33课
### import random
```python
import random

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

```

```
import random:bring in methods from random class
```
```
person:inherits person and animal atttributes
```
```
self.major=major:add new data
```
```
random.random():- i looked up how to use the random class in the python docs
- random() method gives back float in [0,1]
```

```python
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
```

```
animal:parent class
```

```
tag:class variale
```
```
self.rid=rabbit.tag:instance variable
```
```
zfill(3):method on a string to pad the beginning with zeros for example,001 not 1
```
```
def def def :-getter methods specific
for a rabbit class
-there are also getters
get_name and get_age inherited from animal
```