# def int2(x,base=2):
#     return int(x,base)

# import functools
# int2=functools.partial(int,base=2)
# print(int2('1000000'))
import functools
max2=functools.partial(max,10)
print(max2(5,6,45))