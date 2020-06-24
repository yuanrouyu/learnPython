def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def fac(n):
    return fac_iter(n,1)
def fac_iter(num,pro):
    if num==1:
        return pro
    return fac_iter(num-1,num*pro)