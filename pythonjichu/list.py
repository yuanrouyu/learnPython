classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
len(classmates)
print(classmates[0])
print(classmates[-1])
classmates.append("adam")
print(classmates)
classmates.insert(1,"jack")
print(classmates)
classmates.pop() #删除末尾
print(classmates)
classmates.pop(1) #删除第一个
classmates[1]="sarah" #更改

s=["python","java",["asp","php"],"scheme"] #list元素可以是另一个list
n=len(s)
print(n)

p=["a","b"]
b=["c","k",p,"o"]


classmates=('Michael', 'Bob', 'Tracy')
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改,classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
t = (1, 2)
f=()
g=(1) #错误 1
g=(1,) #(1,)




t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#指向不变，内容可变




#打印指定元素
L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
print(L[0][0])
print(L[1][1])
print(L[2][2])