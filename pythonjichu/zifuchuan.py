x=ord('A')
print(x)
y=ord('中')
print(y)
z=chr(66)
print(z)
q=chr(25991)
print(q)
print('\u4e2d\u6587')
print(len('ABC'))
print(len('中文'))
w=len('中文'.encode('utf-8'))
print(w)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
print('Hello, {0:}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
s1 = 72
s2 = 85
r=(s2-s1)/s1
print('%.1f %%' % r)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))