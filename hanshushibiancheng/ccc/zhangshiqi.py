# def log(text):
#     def decor(func):
#         def wrap(*a,**b):
#             print("%s %s()" %(text,func.__name__))
#             return func(*a,**b)
#         return wrap
#     return decor
# @log("madeqisile")
# def now():
#     print("2020.8.16")
# print(now())

# import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

import  time ,functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# @log("madeqisile")
# def now():
#     print("2020.8.16")
# print(now())


# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kw):
#         s=time.time()
#         e=time.time()
#         print('%s executed in %s ms' % (fn.__name__, e-s))
#         return fn(*args,**kw)
#     return wrapper
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)


# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


def metric(fn):
    @functools.wraps(fn)
    def wrap(*a,**b):
        s=time.time()
        e=time.time()
        w=e-s
        print("%s excuted in %s ms"%(fn.__name__,w))
        return fn(*a,**b)
    return wrap
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)


if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

        
