# class student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#     def f(self):
#         print(self.__name,self.__score)
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_score(self,score):
#         self.__score=score
#     def set_name(self,name):
#         self.__name=name
# bart=student('bart',100)

# print(bart._student__score)


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
