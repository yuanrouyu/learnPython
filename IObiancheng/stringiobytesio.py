# from io import StringIO
# f=StringIO()
# print(f.write('hello'))
# print(f.getvalue())



# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
    # print(s.strip())

from io import BytesIO
f=BytesIO()
a=f.write('中文'.encode('utf-8'))
print(a)
print(f.getvalue())