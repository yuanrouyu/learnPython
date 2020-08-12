# L=[]
# for i in range(1,11):
#     L.append(i*i)
# print(L)


# l=[i*i for i in range(1,11)]
# print(l)

# q=[m+n for m in 'ABC' for n in 'XYZ']
# print(q)

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k,v in d.items():
#     print(k,"=",v)


# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# p=[k +"="+v for k,v in d.items()]
# print(p)

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([i.lower() for i in L])

# print([x for x in range(1,11) if x%2==0])
# print([x if x%2==0 else -x for x in range(1 ,11)])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[i.lower() for i in L1 if isinstance(i, str)==True]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
