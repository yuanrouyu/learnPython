def myabs(x):
    if x>=0:
        return x
    else:
        return -x

print(myabs(-500))

def youabs(x):
    if not isinstance(x,(int,float)):  #isinstance（） 内置函数,只允许整数和浮点数
        raise TypeError("bad operatand type")
    if x>=0:
        return x
    else:
        return -x

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y=move(100,100,60,math.pi/6)
print(x,y)