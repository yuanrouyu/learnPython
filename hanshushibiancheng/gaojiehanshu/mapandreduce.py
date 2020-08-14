map/reduce

def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
# r=[f(x) for x in range(1,10)]
# print(r)

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

reduce(f,[z,x,c,v,b])=f(f(f(f(z,x),c),v),b)
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4]))

sum=0
for i in range(1,5):
    sum=sum+i
print(sum)

from functools import reduce
def f(x,y):
    return x*10+y

def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]
# reduce(f,map(char2num,'13579'))
print(list(map(char2num,'13579')))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def srt2int(s):    
    def f2(x,y):
        return x*10+y
    def f1(s):
        return DIGITS[s]
    return reduce(f2,map(f1,s))

def normalize(name):
    name=name[0].upper()+name[1:].lower()
    return name 

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
 
from functools import reduce

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('123.456'))

def str2float(s):
    def f(x,y):
        return x*10+y
    n=s.index(".")
    l1=list(map(int,s[:n]))
    l2=list(map(int,s[n+1:]))
    return reduce(f,l1)+reduce(f,l2)/1000
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



def str2float(s):
    n=s.index(".")
    l1=s[:n]
    l2=s[n+1:]
    L1=list(map(int,l1))
    L2=list(map(int,l2))
    def f(x,y):
        return x*10+y
    return reduce(f,L1)+reduce(f,L2)/1000
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
    