def is_even(n):
    if n>0 and n%2==0:
        return True
    elif n<0 and n%2==0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(-4))
print(is_even(5))
print(is_even(0))

