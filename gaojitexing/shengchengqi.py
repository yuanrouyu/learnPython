# g=(x*x for x in range (10))
# print(g)
# for i in g:
#     print(i)
 
# def f(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done' 
# print(f(6))


# def f(max):
#     n,a,b=0,0,1
#     while n < max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done' 
# f=f(6)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))



# def odd():
#     print('step 1')
#     yield (1)
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o=odd()
# next(o)
# next(o)


# def f(max):
#     n,a,b=0,0,1
#     while n < max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done' 
# for i in f(6):
#     print(i)


# def triangles():
#     l=[1]
 
#     while  True:
#         yield l
#         l=[l[i]+l[i+1] for i in range(len(l)-1)]
#         l.insert(0,1)
#         l.append(1)
# n=0        
# result=[]
# for i in triangles():
#     result.append(i)
#     n=n+1
#     if n== 10:
#         break
# for i in result:
#     print(i)



