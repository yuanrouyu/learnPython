# class student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

# bart=student('bart simpson',59)
# # print(bart.name)
# # print(bart.score)


# def printscore(x):
#     print('%s: %s' % ( x.name, x.score))
# printscore(bart)


class student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def f(self):
        print(self.name)
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

# bart=student('yuanruoyu',100)
# print(bart.name)
# print(bart.score)
# f(bart)
# bart.f()
# print(bart.get_grade())
lisa=student('lisa',99)
bart=student('bart',59)
print(lisa.name,lisa.get_grade())
print(bart.name,bart.get_grade())

