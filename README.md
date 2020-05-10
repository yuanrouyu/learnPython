# learn python
## 第17课 
### Tuples
```python
(2,"mit",3)+(5,6)   (2,"mit",3,5,6)
t=(2,"mit",3)
print(t[1:2])
print(t[1:3])
```

('mit',)  extra comma means a tuple with one element
('mit', 3)
### swap
```python
temp=x
x=y
y=temp

(x,y)=(y,x)
```

```python

def quot_and_remainder(x,y):
    q=x//y
    r=x%y
    return (q,r) 
(quot,rem)=quot_and_remainder(4,5)

```
#### manipulating tuples

```python
def get_data(aTuple):
    nums=()
    words=()
    for t in aTuple:
        nums=nums+(t[0],)
        if t[1] not in words:
            words =words+(t[1],)
    min_n=min(nums)
    max_n=max(nums)
    unique_words=len(words)
    return (min_n,max_n,unique_words)

test=((1,"a"),(2,"b"),(1,"a"),(7,"b"))
(a,b,c)=get_data(test)
print("a:",a,"b:",b,"c:",c)

```
a: 1 b: 7 c: 2
### indices&ordering
```python
L=[2,'a',4,[1,2]]
len(L)
L[0]  
L[2]+1
L[3]
i=2
L[i-1]
print(len(L),L[0],L[2]+1,L[3],L[i-1] )
```
4 2 5 [1, 2] a
###change
```python
L=[2,1,3]
L[1]=5
```
[2,5,3]
###ADD
```python
L1=[2,3,4]
L1.extend([0,6])
print(L1)
```
[2, 3, 4, 0, 6]


```python
L=[1,2,3,4,5]
total=0
for i in range(len(L)):
    total+=L[i]  
    print(total) 
    
L1=[2,1,3,4,3,7,2]
L1.extend([0,6])
print(L1)
L1.remove(2)
print(L1)
del(L1[1])
print(L1)
L1.pop()
print(L1)
```
1
3
6
10
15
[2, 1, 3, 4, 3, 7, 2, 0, 6]
[1, 3, 4, 3, 7, 2, 0, 6]
[1, 4, 3, 7, 2, 0, 6]
[1, 4, 3, 7, 2, 0]

###split
```python
s="I<3 CS"
list(s)
d=s.split('<')
print(d)
L=['a','b','c']
A=''.join(L)
print(A)
B='_'.join(L)
print(B)
```
['I', '3 CS']
abc
a_b_c