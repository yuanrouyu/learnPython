def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return sv

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end(L=[]):
    L.append('END')
    return L