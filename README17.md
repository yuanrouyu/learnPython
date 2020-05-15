# 第17课补充
## 排序
```python
L=[9,6,0,3]
sorted(L)

L.sort()
print(L)
L.reverse()
print (L)
```
## 结果
## [0, 3, 6, 9]
## [9, 6, 3, 0]
## 添加
```python
warm=['red','yellow','orange']
hot=warm
hot.append('pink')
print(hot)
print(warm)

cool=['blue','green','grey']
chill=cool[:]
chill.append('black')
print(chill)
print(cool)


warm=['red','yellow','orange']
sortedwarm=warm.sort()
print(warm)
print(sortedwarm)
cool=['grey','green','blue']
sortedcool=sorted(cool)
print(cool)
print(sortedcool)
```
warm也被改变，先chill=cool[:]才可以保持不变
sortedwarm=warm.sort()不会输出sortedwarm，要用sortedcool=sorted(cool)
## 结果
## ['red', 'yellow', 'orange', 'pink']
## ['red', 'yellow', 'orange', 'pink']
## ['blue', 'green', 'grey', 'black']
## ['blue', 'green', 'grey']
## ['orange', 'red', 'yellow']
## None
## ['grey', 'green', 'blue']
## ['blue', 'green', 'grey']
```python
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups(L1,L2)
print(L1)


def remove_dups(L1,L2):
    L1_copy=L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups(L1,L2)
print(L1)
```
先要复制原来的 L1_copy=L1[:]
## 结果
## [2, 3, 4]
## [3, 4]
