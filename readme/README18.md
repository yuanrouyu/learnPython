# 第18课
## tuple 和string的区别
```python
def always_sunny(t1,t2):
    sun=("sunny","sun")
    first=t1[0]+t2[0]
    return(sun[0],first)

print(always_sunny(('cloudy'),('cold',)))
```
### ('sunny', 'ccold')

#### t1='cloudy'---  string
#### t2='cold', ---  tuple
#### first='c'+'cold'