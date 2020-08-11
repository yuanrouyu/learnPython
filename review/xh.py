menu = ['duck','fish','tomato']
for i in menu:
    print(i)


#1-100 add

sum=0
for i in range(101):
    sum=sum+i
print(sum)


#奇数和

sum=0
for i in range(101):
    if i%2==0:
        continue
    sum=sum+i
print(sum)


sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

#依次打印hello,xxx!
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print("Hello",i,"!")

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')