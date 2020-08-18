# print(type(123))

# class mydog(object):
#     def __len__(self):
#         return 100
# dog=mydog()
# print(dog.__len__())
# print(len(dog))


class myobject(object):
    def __init__(self):
        self.zhi=9
    def power(self):
        return self.zhi*self.zhi
obj=myobject()
print(hasattr(obj,'zhi'))
print(hasattr(obj,'name'))
setattr(obj,'name',19)
print(hasattr(obj,'name'))
print(getattr(obj,'name'))
print(obj.power())