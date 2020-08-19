# class Hello(object):
#     def hello(self,name='world'):
#         print('hello,%s.' % name)
# from yuanlei import Hello
# h=Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

def fn(self, name='world'):
    print('Hello, %s.' % name)
Hello=type('Hello',(object,),dict(hell=fn))
h=Hello()
h.hell()


super函数补充：https://www.runoob.com/python/python-func-super.html
Metaclass：https://www.cnblogs.com/ArsenalfanInECNU/p/9036407.html
还有ORM：https://www.cnblogs.com/ArsenalfanInECNU/p/9100874.html