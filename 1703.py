
#L=[2,'a',4,[1,2]]
#len(L)
#L[0]  
#L[2]+1
#L[3]
#i=2
#L[i-1]
#print(len(L),L[0],L[2]+1,L[3],L[i-1] )
#L=[2,1,3]
#L[1]=5
#print(L)

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


s="I<3 CS"
list(s)
d=s.split('<')
print(d)
L=['a','b','c']
A=''.join(L)
print(A)
B='_'.join(L)
print(B)

