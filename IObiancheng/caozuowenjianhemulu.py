import os
# print(os.uname)
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x','default'))

print(os.path.abspath('.'))
print(os.path.join('/mnt/c/alaji/learnPython', 'testdir'))
# os.mkdir('/mnt/c/alaji/learnPython/testdir')
os.rmdir('/mnt/c/alaji/learnPython/testdir') 

os.path.split('/Users/michael/testdir/file.txt')
os.path.splitext('/path/to/file.txt')
os.rename('test.txt', 'test.py')
s.remove('test.py')
[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

def main():

    findname = input()  # 输入要查找的指定字符串的文件名字

    toTheFolers('.', findname)


#该方法用于在文件夹内寻找是否含有该文件

def toTheFolers(basepath, findname):

    for name in os.listdir(basepath):

        file_name = os.path.splitext(name)[0]   #拆分开来

        path = os.path.join(basepath, name)     #某个文件或者文件夹的相对路径

        if(file_name == findname):              #如果某个文件夹的名字符合也要输出

            print(path)