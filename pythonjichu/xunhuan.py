names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

list(range(5))
#[0, 1, 2, 3, 4]
#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数


sum=0
for x in range(100):
    sum=sum+x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


L = ['Bart', 'Lisa', 'Adam']

for x in L:
    print("hello",x)



n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')





n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')



n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
