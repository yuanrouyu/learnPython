L=[9,6,0,3]
sorted(L)

L.sort()
print(L)
L.reverse()
print (L)


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


