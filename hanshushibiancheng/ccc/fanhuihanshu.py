# def qiuhe(*x):
#     sum=0
#     for n in x:
#         sum=sum+n
#     return sum

# def lazysum(*x):
#     def sum():
#         a=0
#         for n in x:
#             a=a+n
#         return a
#     return sum
# f=lazysum(1,3,5,7,9)
# print(f())
    

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def createCounter():
    l=[0]
    def counter():       
        l[0]=l[0]+1
        return l[0]
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')