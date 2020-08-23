import re
a=re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(a)

b=re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(b)


test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.group(0)
m.group(1)
m.group(2)


re.match(r'^(\d+)(0*)$', '102300').groups()
re.match(r'^(\d+?)(0*)$', '102300').groups()


# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
re_telephone.match('010-12345').group()