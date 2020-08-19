from enum import Enum

m = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name ,member in m.__members__.items():
    print(name,'=>',member,',',member.value)

from enum import Enum,unique
@unique
class weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# day1=weekday.Mon
# print(day1)
# day11=weekday['Mon']
# print(day11)
# day111=weekday.Mon.value
# print(day111)
# print(weekday(1))
for name,member in weekday.__members__.items():
    print(name,member)

# from enum import Enum,unique
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
# # print(bart.gender)
# # print(Gender.Male)