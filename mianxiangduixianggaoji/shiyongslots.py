# class student(object):
#     pass

# # s.name='xiaoming'
# # print(s.name)
# def setage(self,age):
#     self.age=age
# s=student()
# s2=student()
# from types import MethodType
# s.setage=MethodType(setage,s)
# s2.setage=MethodType(setage,s2)
# s.setage(25)
# s2.setage(26)
# print(s.age)
# print(s2.age)
# class student(object):
#     pass
# def set_score(self,score):
#     self.score=score
# student.set_score=set_score
# s=student()
# s2=student()
# s.set_score(100)
# print(s.score)
# s2.set_score(99)
# print(s2.score)


class student(object):
    __slots__=('name','age')
s=student()
s.name='xiaoming'
s.age=25
# s.score=99
print(s.name)
