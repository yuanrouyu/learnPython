
def trim(s):
    if 0==len(s):
        return s

    while ' '==s[0]:
        s=s[1:]
        if 0==len(s):
            return s
        
    while ' '==s[-1]:
        s=s[:-1]
        
  

    return s
  

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
