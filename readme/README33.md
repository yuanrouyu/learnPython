## 33课
### how to define a class
```python
class animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
```

```
class:class definition
```

```
animal:name
```

```
object:class parent
```

```
__init__:special method to create an instance 
```

```
self:variable to refer to an instance of the class

```

```python
def set_name(self,newname=""):
    self.name=newname
```

```python
a=animal(3)
a.set_name("")
print(a.get_name())
```
```
""
```

```python
a=animal(3)
a.set_name("fluffy")
print(a.get_name())
```
```
fluffy
```

