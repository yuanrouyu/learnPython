
try:
    f = open('/mnt/c/alaji/learnPython/666.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/mnt/c/alaji/learnPython/666.py', 'r') as f:
    print(f.read())


    for line in f.readlines():
        print(line.strip())


f = open('/mnt/c/alaji/learnPython/2020-05-26.png', 'rb')
print(f.read())

f = open('/mnt/c/alaji/learnPython/666.py', 'r', encoding='gbk',errors='ignore')
print(f.read())

f = open('/mnt/c/alaji/learnPython/666.py', 'w')
print(f.write('yuanruoyu'))
f.close()


with open('/mnt/c/alaji/learnPython/666.py', 'w') as f:
    f.write('Hello, world!')