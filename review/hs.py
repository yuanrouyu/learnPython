
# 一元二次方程
import math
def aaa(a,b,c):
    x=(-1*b+math.sqrt(b*b-4*a*c))/(2*a)
    y=(-1*b-math.sqrt(b*b-4*a*c))/(2*a)
    return x,y
print('aaa(2, 3, 1) =', aaa(2, 3, 1))

#power

def power(x,n):
    s=1
    for i in range(n):
        s=s*x
    return s
print(power(2,10))


def f2(a, b, c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'kw =', kw)
args = (1, 2, 3)
kw = {'g': 88, 'x': '#'}
print(f2(*args, **kw))