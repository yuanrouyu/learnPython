def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5,2))


def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(5))

def enroll(name,gender):
    print("name",name)
    print("gender",gender)

enroll("sarah","f")


def add(l=None):
    if l is None:
        l=[]
    l.append("end")
    return l


print(add([1,2,3]))


def cal(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(cal([1,2,3]))


def cal(*numbers):
    sum=0
    for n in numbers:
        sum =sum+n*n
    return sum

print(cal(1,2))
print(cal())

nums=[1,2,3]
cal(nums[0],nums[1],nums[2])
cal(*nums)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Bob', 35, city='Beijing')


extra={"city":"beijing","job":"engineer"}
person("jack",24,city=extra["city"],job=extra["job"])
person("jack",24,**extra)