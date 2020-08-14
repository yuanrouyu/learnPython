# def odd(n):
#     return n%2==1
# print(list(filter(odd,[1,2,4,5,6,9,10])))

# def f(s):
#     return  s and s.strip()
# print(list(filter(f,['a','','b',None,'c','  '])))



# def not_empty(s):

#     return s and s.strip()

# print(list(filter(not_empty,[' C'])))


# def odd():
#     n=1
#     while True:
#         n=n+2
#         yield n
# def div(n):
#     return lambda x: x % n > 0
# def primes():
#     yield 2
#     it=odd()
#     while True:
        
#         n=next(it)
#         yield n
#         it=filter(div(n),it)
# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break

def is_palindrome(n):
    nn=str(n)
    return nn==nn[::-1]
    print (list(filter(is_palindrome,range(1,1000))))
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')