# class student (object):
    
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
# # print(student('xiaoming'))
# s=student('xiaoming')

# # s.name='xiaoming'

# print(s.name)

# class fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>100000:
#             raise StopAsyncIteration()
#         return self.a 
# class fib(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# f=fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[3])
# print(f[4])
# # for n in fib():
# #     print(n)


# class fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b 
#             return a 
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             l=[]
#             for x in range(stop):
#                 if x>=start:
#                     l.append(a)
#                 a,b=b,a+b
#             return l
# f=fib()
# print(f[2:8])


# class student(object):
#     def __init__(self):
#         self.name='xiaoming'
#     def __getattr__(self,attr):
#         if attr=='score':
#             return 99
#     def __getattr__(self,attr):
#         if attr=='age':
#             return lambda:25
# s=student()
# print(s.name)
# print(s.score)
# print(s.age())


# class chain(object):

#     def __init__(self,path=''):
#         self._path=path

#     def __getattr__(self,path):
#         return chain('%s/%s'%(self._path,path))

#     def __str__(self):
#         return self._path

#     __repr__=__str__

# print(chain().status.user.timeline.list)


# class Chain(object):

#     def __init__(self, path=''):
#         self._path = path

#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))

#     def __str__(self):
#         return self._path

#     __repr__ = __str__


# print(Chain().status.user.timeline.list)

# class student(object):
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         print(self.name)
# s=student('xiaoming')
# s()



# >>> callable(Student())
# True
# >>> callable(max)
# True
# >>> callable([1, 2, 3])
# False
# >>> callable(None)
# False
# >>> callable('str')
# False


class Chain(object):
    def __init__(self, path=''):
       self.__path = path

   def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))

   def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

   def __str__(self):
       return self.__path

   __repr__ = __str__

   print(Chain().users('michael').repos) # /users/michael/repos