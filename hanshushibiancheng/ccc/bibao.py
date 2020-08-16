#比较1，fs返回的是list格式的3个函数[f(), f(), f()], 此时的函数f()中的变量i为range(1,4)的最终值3
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)  #此处为f函数    
    return fs
f1, f2, f3 = count()
f1, f2, f3 #输出3个相同引用状态的f()函数f1(), f2(), f3() #输出3个相同的， 当i=3时刻对应的f()函数值， 即f(3)=9

#比较2，fs返回的是list格式的3个函数值[f(1), f(2), f(3)], 对于不同i值， f(i)函数即时返回i在每个generator对应函数值f(i)
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs
f1, f2, f3 = count()
f1, f2, f3 #输出i分别为1/2/3时刻对应的f函数值(1, 4, 9)f1(), f2(), f3() #报错，因为此时count()函数直接输出函数值，不是输出函数

#比较3，fs返回的是list格式的3个函数[f(i), f(i), f(i)], 此处的内函数f(i)中的i却不同， 因为f(i)返回的是不同i值对应的g()函数， 即f(i)函数即时返回i在每个generator对应g()函数
def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i*i
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
f1, f2, f3 #分别输出3个不同的函数， i=1/2/3时刻对应的3个f(i)函数, 这3个f(i)函数返回不同的g函数（变量i不同）f1(), f2(), f3() #输出(1, 4, 9)
对于闭包练习题目的理解

# 闭包计数器函数1-a， 报错方案
def createCounter():
    i = 0 # 此处i在外函数定义， 因为内函数引用了i， 变量i会保存在内容中    
    def counter():
        i += 1 # 内函数引用i， 但是不可以改变i值，因为i一直保存在内存中        
        return i
    return counter

# 闭包计数器函数1-b， 解决办法
def createCounter():
    i = 0 # 此处i在外函数定义， 因为内函数引用了i， 变量i会保存在内容中    
    def counter():
        nonlocal i #Python 3.x可以声明变量i为局部变量        
        i += 1 # 声明后变量i可以修改        
        return i
    return counter

# 闭包计数器函数2-a， 选择数值可变但是地址不变的变量类型——数组
def createCounter():
    i = [0] # 初始化数组    
    def counter():
        i[0] += 1 #不修改数组， 尽修改数组中元素数值， 数组的地址不变        
        return i[0]
    return counter

# 闭包计数器函数2-b， 也可以选择dict类型变量，与数组同理， 主要不改变变量引用地址即可
def createCounter():
    i = {'a':0}
    def counter():
        i['a'] += 1        
        return i['a']
    return counter