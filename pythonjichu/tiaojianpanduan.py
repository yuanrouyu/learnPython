age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


s = input('birth: ')
birth = int(s) #input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
if birth < 2000:
    print('00前')
else:
    print('00后')

height = 1.75
weight = 80.5
bim=weight/height/height
if bim<18.5:
    print("过轻")
elif 18.5<=bim<25:
    print("正常")
elif 25<=bim<28:
    print("过重")
elif 28<=bim<32:
    print("肥胖")
else:
    print("严重肥胖")