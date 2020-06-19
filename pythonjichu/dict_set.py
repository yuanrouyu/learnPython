d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])


d['Adam'] = 67
print(d['Adam'])

d.get('Thomas')
d.get('Thomas', -1)

d.pop('Bob')
print(d) #{'Michael': 95, 'Tracy': 85}


s = set([1, 2, 3])
print(s)

s = set([1, 1, 2, 2, 3, 3])
print(s)
 #传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
s.add(4)
s.remove(4)


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) #{2,3}
print(s1 | s2) #{1,2,3,4}


a = ['c', 'b', 'a']
a.sort()
print(a)
#['a', 'b', 'c']

a = 'abc'
a.replace('a', 'A')
print(a)
#'Abc'

a = 'abc'
b = a.replace('a', 'A')
print(b)
#'Abc'
print(a)
#'abc'

