# class animal(object):
#     def run(self):
#         print('animal is running')
# class dog(animal):
#     pass
# class cat(animal):
#     pass
# dog=dog()
# dog.run()
# cat=cat()
# cat.run()
class animal (object):
    def run(self):
        print('animal is running')
    def eat(self):
        print('animal is eating')
  
class dog(animal):
    def run(self):
        print('dog is running')
    pass
class cat(animal):
    def run(self):
        print('cat is running')
    pass
class tortoise(animal):
    def run(self):
        print('tortoise is running slowly')
def run_twice(x):
    x.run()

print(run_twice(animal()))
print(run_twice(dog()))
print(run_twice(tortoise()))


a = list() # a是list类型
b = animal() # b是Animal类型
# c = dog() # c是Dog类型
print(type(b))
print(type(a))



# dog=dog()
# cat=cat()
# dog.run()
# cat.run()