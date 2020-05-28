## 27课
## wrapping your head around types and classes
```python
    c=Coordinate(3,4)
    print(c)
    print(type(c))


<3,4>
<class __main__.Coordinate>
```

retun of the _str_ method
the type of object c is a class Coordinate

```python
    print(Coordinate)
    print(type(Coordinate))


<class __main__.Coordinate>
<class 'type'>
```

a Coordinate is a class
a Coordinate class is a type of object

```python
    print(isinstance(c,Coordinate))


True
```

## special operators
```python
class Fraction(object):
    def __init__(self,num,denom):
        assert type(num)==int and type(denom)==int 
        self.num=num
        self.denom=denom
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    def __add__(self,other):
        top=self.num*other.denom+self.denom*other.num
        bott=self.denom*other.denom
        return Fraction(top,bott)
    def __sub__(self,other):
        top=self.num*other.denom-self.denom*other.num
        bott=self.denom*other.denom
        return Fraction(top,bott)
    def __float__(self):
        return self.num/self.denom
    def inverse(self):
        return Fraction(self.denom,self.num)
a=Fraction(1,4)
b=Fraction(3,4)
c=a+b
d=b.inverse()
f=a-d
print(f)
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
```
-13/12
16/16
1.0
1.0
1.3333333333333333

a=1/4,b=3/4
c=a+b:  top=1*4+3*4=16,bott=4*4=16,Fraction(16,16) 16/16
![Image text](tttt/own_method.png)
![Image text](tttt/special_operators.png)
![Image text](https://github.com/yuanrouyu/learnPython/blob/master/tttt/types%20_and_class.png)
![Image text](tttt/use_a_method.png)
