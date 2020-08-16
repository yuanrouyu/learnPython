# def f(i):
#     return i*i
# l=[]
# for i in range(1,4):
#     l.append(f(i))
# print(l)

# f=list(i*i for i in range(1,4))
# print(f)

# def f(i):
#     return i*i
# print(list(map(f,[1,2,3])))

# f=list(map(lambda x:x*x,[1,2,3]))
# print(f)

# f=lambda x: x*x
# print(f(5))

# def build(x,y):
#     return lambda:x*x+y*y


def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))


l=list(filter(lambda n:n%2==1,range(1,20)))
print(l)